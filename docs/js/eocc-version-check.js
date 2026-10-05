/* EOCC 文档站 —— 站点版本检测与更新提醒
 *
 * 作用：
 *   1. 读取站点版本数据（默认 data/site-info.json，路径由 <html data-site-info> 或脚本 data-src 指定）
 *   2. 把云端版本号写入 Cookie（eocc_site_version）
 *   3. 若 Cookie 中的「上次访问版本」与云端版本不一致，弹出**非全屏侵入式**提醒：
 *      上次访问版本 → 现在版本
 *
 * 纯原生 JS，不依赖任何外部库；样式位于 css/eocc-brand.css（.md-version-* 命名空间）。
 * connor：不阻塞页面渲染，脚本以 defer 方式引入。
 */
(function () {
  "use strict";

  var COOKIE_NAME = "eocc_site_version";
  var COOKIE_DAYS = 365;
  var BANNER_DELAY = 1200; // 首访不打扰，稍后再提示

  /* ---------- Cookie 读写 ---------- */

  function readCookie(name) {
    var key = name + "=";
    var parts = document.cookie ? document.cookie.split("; ") : [];
    for (var i = 0; i < parts.length; i++) {
      if (parts[i].indexOf(key) === 0) {
        return decodeURIComponent(parts[i].substring(key.length));
      }
    }
    return "";
  }

  function writeCookie(name, value, days) {
    var d = new Date();
    d.setTime(d.getTime() + days * 24 * 60 * 60 * 1000);
    document.cookie =
      name + "=" + encodeURIComponent(value) +
      "; expires=" + d.toUTCString() +
      "; path=/; SameSite=Lax";
  }

  /* ---------- 数据源路径 ---------- */

  function resolveSrc() {
    // 优先取脚本自身的 data-src（由构建/模板按页面层级写入相对路径）
    var self = document.currentScript;
    if (self && self.getAttribute("data-src")) return self.getAttribute("data-src");
    // 回退：由 <html data-site-info="..."> 指定
    var root = document.documentElement.getAttribute("data-site-info");
    if (root) return root;
    // 最终回退：站点根绝对路径（GitHub Pages 部署在域名根目录）
    return "/data/site-info.json";
  }

  /* ---------- 侧边栏版本号回填 ---------- */

  function fillSidebarVersion(curr) {
    var nodes = document.querySelectorAll(".md-sidebar-meta__ver-num");
    for (var i = 0; i < nodes.length; i++) nodes[i].textContent = curr;
  }

  /* ---------- 提醒条（非全屏、右下角浮层，可关闭） ---------- */

  function showBanner(prev, curr, updated) {
    if (document.querySelector(".md-version-banner")) return;

    var box = document.createElement("div");
    box.className = "md-version-banner";
    box.setAttribute("role", "status");
    box.setAttribute("aria-live", "polite");

    var title = document.createElement("p");
    title.className = "md-version-banner__title";
    title.textContent = "文档站已更新";

    var desc = document.createElement("p");
    desc.className = "md-version-banner__desc";
    // 「上次访问版本 → 现在版本」
    var from = prev ? prev : "首次访问";
    var arrow = document.createElement("span");
    arrow.className = "md-version-banner__arrow";
    arrow.textContent = " → ";
    desc.appendChild(document.createTextNode("上次访问版本 " + from));
    desc.appendChild(arrow);
    desc.appendChild(document.createTextNode(" 现在版本 " + curr));
    if (updated) {
      var t = document.createElement("span");
      t.className = "md-version-banner__time";
      t.textContent = "（更新于 " + updated + "）";
      desc.appendChild(t);
    }

    var actions = document.createElement("div");
    actions.className = "md-version-banner__actions";

    var link = document.createElement("a");
    link.className = "md-version-banner__link";
    link.href = "release/";
    link.textContent = "查看更新日志";

    var close = document.createElement("button");
    close.type = "button";
    close.className = "md-version-banner__close";
    close.setAttribute("aria-label", "关闭提醒");
    close.textContent = "知道了";
    close.addEventListener("click", function () { box.remove(); });

    actions.appendChild(link);
    actions.appendChild(close);
    box.appendChild(title);
    box.appendChild(desc);
    box.appendChild(actions);

    // 链接按页面层级修正
    var depth = (location.pathname.replace(/[^/]*$/, "").match(/\//g) || []).length - 1;
    if (depth > 0) link.href = "../".repeat(depth) + "release/";

    setTimeout(function () { document.body.appendChild(box); }, BANNER_DELAY);
  }

  /* ---------- 主流程 ---------- */

  function run() {
    var src = resolveSrc();
    fetch(src, { cache: "no-store" })
      .then(function (res) {
        if (!res.ok) throw new Error("HTTP " + res.status);
        return res.json();
      })
      .then(function (data) {
        var site = (data && data.site) || {};
        var curr = site.version || "";
        if (!curr) return;

        var prev = readCookie(COOKIE_NAME);
        // 版本变化：仅在确实记录过旧版本、且与当前不一致时提示
        if (prev && prev !== curr) showBanner(prev, curr, site.updated);
        // 回填侧边栏标题下方的版本号（各页保留的静态值仅作无 JS 时的兜底）
        fillSidebarVersion(curr);
        // 始终把当前版本写入 Cookie，作为「上次访问版本」
        writeCookie(COOKIE_NAME, curr, COOKIE_DAYS);
      })
      .catch(function () {
        /* 静默失败：版本检测不应影响页面正常使用 */
      });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", run);
  } else {
    run();
  }
})();
