function toggleFAQ(item) {
  item.classList.toggle("active");
}

document.addEventListener("DOMContentLoaded", () => {
  const faqItems = document.querySelectorAll(".faq-item");

  faqItems.forEach(item => {
    item.addEventListener("click", () => toggleFAQ(item));
  });

  const elements = document.querySelectorAll(".typewriter");

  elements.forEach((el, index) => {
    const text = el.textContent.trim();
    el.textContent = ""; 
    el.style.opacity = "1";

    let i = 0;

    function typeChar() {
      if (i < text.length) {
        el.textContent += text.charAt(i);
        i++;
        setTimeout(typeChar, 28);
      }
    }
    setTimeout(typeChar, index * 850);
  });
});

window.addEventListener("scroll", () => {
  const navbar = document.querySelector(".navbar");

  if (window.scrollY > 500) {
    navbar.classList.add("scrolled");
  } else {
    navbar.classList.remove("scrolled");
  }
  const menuBtn = document.getElementById("menuBtn");
  menuBtn.addEventListener("click", () => {
    navbar.classList.toggle("open");
  });
});

