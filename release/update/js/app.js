/* EOCCC release notes renderer — GitHub Pages 静态版 */
(function () {
  "use strict";
  var logsEl = document.getElementById("logs");
  var currentFilter = "all";
  var releases = [];

  function typeLabel(t) {
    return { release: "正式发布", update: "功能更新", bugfix: "问题修复", notice: "公告" }[t] || t;
  }
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function fmtTime(s) {
    // 源时间为北京时间(UTC+8)，展示时保持原样并标注时区
    return esc(s) + "（北京时间）";
  }

  function card(r, idx) {
    var badges = '<span class="badge ' + esc(r.type) + '">' + esc(typeLabel(r.type)) + "</span>";
    if (r.pin) badges += '<span class="badge pin">置顶</span>';
    if (r.hot) badges += '<span class="badge hot">热门</span>';
    var ver = r.version ? esc(r.version) + " · " : "";
    // 注意：卡片一律以「收起」状态渲染。
    // 置顶仅用角标表示，不再初始带 open 类——否则被置顶的历史日志会被自动展开，
    // 用户未点击却在页面加载时就加载了它的正文，表现为「其他分支被异常展开」。
    // data-idx 记录该卡片在当前筛选列表中的序号，供点击/深链时取回数据，避免依赖 DOM 顺序假设。
    var html =
      '<article class="log" data-idx="' + idx + '" data-type="' + esc(r.type) + '">' +
      '<div class="log-head"><h2>' + ver + esc(r.title) + "</h2>" + badges + "</div>" +
      '<div class="log-meta">发布：' + fmtTime(r.publish_time) + " · 作者：" + esc(r.author) + "</div>" +
      '<p class="log-summary">' + esc(r.summary) + "</p>" +
      '<div class="log-actions">' +
      '<button class="btn primary" data-act="toggle">展开详情</button>' +
      '<span class="log-links">' +
      (r.links && r.links.download_page
        ? '<a class="btn" target="_blank" rel="noopener" href="' + esc(r.links.download_page) + '">下载页面</a>'
        : "") +
      (r.links && r.links.app_page
        ? '<a class="btn" target="_blank" rel="noopener" href="' + esc(r.links.app_page) + '">应用下载</a>'
        : "") +
      (r.links && r.links.github
        ? '<a class="btn" target="_blank" rel="noopener" href="' + esc(r.links.github) + '">GitHub</a>'
        : "") +
      "</span>" +
      "</div>" +
      '<div class="log-body"><span class="md-log-loading">加载中…</span></div>' +
      "</article>";
    return html;
  }

  function render() {
    var list = releases.filter(function (r) {
      return currentFilter === "all" || r.type === currentFilter;
    });
    logsEl.innerHTML = list.length
      ? list.map(card).join("")
      : '<p style="text-align:center;color:var(--muted);padding:40px 0">该分类下暂无日志</p>';
    updateToggleLabels();
  }

  // 统一的「展开/收起」按钮文案同步
  function updateToggleLabels() {
    logsEl.querySelectorAll(".log").forEach(function (article) {
      var btn = article.querySelector("[data-act=toggle]");
      if (btn) btn.textContent = article.classList.contains("open") ? "收起详情" : "展开详情";
    });
  }

  // 由卡片元素取回对应的日志数据（不依赖 children 下标，避免顺序假设出错）
  function dataOf(article) {
    return releases.filter(function (x) {
      return currentFilter === "all" || x.type === currentFilter;
    })[article.dataset.idx];
  }

  function loadBody(article, r) {
    var body = article.querySelector(".log-body");
    if (body.dataset.loaded) return;
    var url = "./md/" + encodeURIComponent(r.md_file) + ".md";
    // 请求阶段临时占位，成功/失败后均移除，禁止常驻
    body.innerHTML = '<span class="md-log-loading">加载中…</span>';
    fetch(url)
      .then(function (res) {
        if (!res.ok) throw new Error("HTTP " + res.status + " @ " + url);
        return res.text();
      })
      .then(function (text) {
        // 修正 md 内相对图片路径：./picture/... → ./picture/...（md 与 picture 同级，保持不变即可）
        body.innerHTML = window.marked ? marked.parse(text) : "<pre>" + esc(text) + "</pre>";
        body.dataset.loaded = "1";
      })
      .catch(function (err) {
        body.innerHTML = '<p style="color:#e07070">加载失败：' + esc(err.message) + "</p>";
        body.dataset.loaded = "1";
      });
  }

  logsEl.addEventListener("click", function (e) {
    var article = e.target.closest(".log");
    if (!article) return;
    var r = dataOf(article);
    if (!r) return;
    if (e.target.matches("[data-act=toggle]")) {
      article.classList.toggle("open");
      if (article.classList.contains("open")) {
        e.target.textContent = "收起详情";
        loadBody(article, r);
      } else {
        e.target.textContent = "展开详情";
      }
    }
  });

  document.getElementById("filters").addEventListener("click", function (e) {
    if (!e.target.matches("button")) return;
    document.querySelectorAll("#filters button").forEach(function (b) {
      b.classList.remove("active");
    });
    e.target.classList.add("active");
    currentFilter = e.target.dataset.f;
    render();
  });

  fetch("./releases.json")
    .then(function (res) {
      if (!res.ok) throw new Error("HTTP " + res.status + " @ releases.json");
      return res.json();
    })
    .then(function (data) {
      releases = data.releases || [];
      // 置顶优先，其余按发布时间倒序（维持版本时序）
      releases.sort(function (a, b) {
        if (a.pin !== b.pin) return b.pin - a.pin;
        return a.publish_time < b.publish_time ? 1 : -1;
      });
      render();
      openFromQuery();
    })
    .catch(function (err) {
      logsEl.innerHTML = '<p style="color:#e07070">数据加载失败：' + esc(err.message) + "</p>";
    });

  // 支持 ?log=<md_file> 直达：自动展开对应日志并滚动定位
  function openFromQuery() {
    var q = new URLSearchParams(location.search).get("log");
    if (!q) return;
    var target = null;
    logsEl.querySelectorAll(".log").forEach(function (article) {
      var r = dataOf(article);
      if (r && r.md_file === q) target = { article: article, r: r };
    });
    if (!target) return;
    target.article.classList.add("open");
    var btn = target.article.querySelector("[data-act=toggle]");
    if (btn) btn.textContent = "收起详情";
    loadBody(target.article, target.r);
    target.article.scrollIntoView({ behavior: "smooth", block: "start" });
  }
})();
