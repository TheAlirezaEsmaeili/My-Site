// باز و بسته کردن منوی موبایل
document.addEventListener("DOMContentLoaded", function () {
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");
  var auth = document.querySelector(".nav-auth");

  if (toggle && links) {
    toggle.addEventListener("click", function () {
      links.classList.toggle("open");
      if (auth) auth.classList.toggle("open");
    });
  }
});
