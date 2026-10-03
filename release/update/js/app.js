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

  function card(r) {
    var badges = '<span class="badge ' + esc(r.type) + '">' + esc(typeLabel(r.type)) + "</span>";
    if (r.pin) badges += '<span class="badge pin">置顶</span>';
    if (r.hot) badges += '<span class="badge hot">热门</span>';
    var ver = r.version ? esc(r.version) + " · " : "";
    var html =
      '<article class="log' + (r.pin ? " open" : "") + '" data-type="' + esc(r.type) + '">' +
      '<div class="log-head"><h2>' + ver + esc(r.title) + "</h2>" + badges + "</div>" +
      '<div class="log-meta">发布：' + fmtTime(r.publish_time) + " · 作者：" + esc(r.author) + "</div>" +
      '<p class="log-summary">' + esc(r.summary) + "</p>" +
      '<div class="log-actions">' +
      '<button class="btn primary" data-act="toggle">展开详情</button>' +
      (r.links && r.links.download_page
        ? '<a class="btn" target="_blank" rel="noopener" href="' + esc(r.links.download_page) + '">下载页面</a>'
        : "") +
      (r.links && r.links.app_page
        ? '<a class="btn" target="_blank" rel="noopener" href="' + esc(r.links.app_page) + '">应用下载</a>'
        : "") +
      (r.links && r.links.github
        ? '<a class="btn" target="_blank" rel="noopener" href="' + esc(r.links.github) + '">GitHub</a>'
        : "") +
      "</div>" +
      '<div class="log-body">加载中…</div>' +
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
  }

  function loadBody(article, r) {
    var body = article.querySelector(".log-body");
    if (body.dataset.loaded) return;
    var url = "./md/" + encodeURIComponent(r.md_file) + ".md";
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
      });
  }

  logsEl.addEventListener("click", function (e) {
    var article = e.target.closest(".log");
    if (!article) return;
    var idx = Array.prototype.indexOf.call(logsEl.children, article);
    var r = releases.filter(function (x) {
      return currentFilter === "all" || x.type === currentFilter;
    })[idx];
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
    })
    .catch(function (err) {
      logsEl.innerHTML = '<p style="color:#e07070">数据加载失败：' + esc(err.message) + "</p>";
    });
})();
