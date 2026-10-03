/* EOCC 文档站 —— 图片放大（示意图/流程图）
   为带 .md-zoomable 的图片提供点击放大预览：点击图片或右下角按钮打开，点击遮罩 / 按 Esc 关闭。
   纯原生 JS，不依赖任何外部库；样式位于 css/eocc-brand.css。 */
(function () {
  "use strict";

  var HINT_TEXT = "点击放大";
  var mask = null;
  var zoomImg = null;
  var caption = null;
  var lastFocus = null;

  function buildMask() {
    mask = document.createElement("div");
    mask.className = "md-zoom-mask";
    mask.setAttribute("role", "dialog");
    mask.setAttribute("aria-modal", "true");
    mask.setAttribute("aria-label", "图片放大预览");

    zoomImg = document.createElement("img");
    zoomImg.alt = "";

    caption = document.createElement("p");
    caption.className = "md-zoom-caption";

    mask.appendChild(zoomImg);
    mask.appendChild(caption);

    // 点击遮罩空白处（或图片本身）关闭
    mask.addEventListener("click", function (e) {
      if (e.target === mask || e.target === zoomImg) close();
    });

    document.body.appendChild(mask);
  }

  function open(src, alt) {
    if (!mask) buildMask();
    zoomImg.src = src;
    zoomImg.alt = alt || "";
    caption.textContent = alt || "";
    mask.classList.add("is-open");
    document.body.classList.add("md-zoom-locked");
    lastFocus = document.activeElement;
    zoomImg.focus();
  }

  function close() {
    if (!mask) return;
    mask.classList.remove("is-open");
    document.body.classList.remove("md-zoom-locked");
    zoomImg.src = "";
    if (lastFocus && lastFocus.focus) lastFocus.focus();
    lastFocus = null;
  }

  // Esc 关闭
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && mask && mask.classList.contains("is-open")) close();
  });

  // 给单张图片加上放大入口
  function enhance(img) {
    if (img.dataset.zoomReady === "1") return;
    img.dataset.zoomReady = "1";
    img.classList.add("md-zoomable");
    img.setAttribute("tabindex", "0");
    img.setAttribute("role", "button");
    img.setAttribute("aria-label", (img.alt || "图片") + "——" + HINT_TEXT);

    img.addEventListener("click", function () {
      open(img.currentSrc || img.src, img.alt);
    });
    // 键盘可达：Enter / 空格
    img.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        open(img.currentSrc || img.src, img.alt);
      }
    });
  }

  function init(root) {
    var scope = root || document;
    // 只放大正文中的示意图，排除头像等小尺寸图标
    var imgs = scope.querySelectorAll("article img:not([data-no-zoom])");
    Array.prototype.forEach.call(imgs, function (img) {
      // 尺寸过小（头像、图标）不参与放大
      var w = img.getAttribute("width");
      if (w && parseInt(w, 10) < 160) return;
      if (img.classList.contains("md-zoomable")) { enhance(img); return; }
      enhance(img);
    });

    // 右下角提示（仅在页面确实存在可放大图片时出现）
    if (document.querySelector("article img.md-zoomable") && !document.querySelector(".md-zoom-hint")) {
      var hint = document.createElement("div");
      hint.className = "md-zoom-hint";
      hint.textContent = "点击图片可放大";
      document.body.appendChild(hint);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () { init(); });
  } else {
    init();
  }
})();
