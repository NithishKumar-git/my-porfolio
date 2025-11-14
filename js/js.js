document.addEventListener("DOMContentLoaded", () => {
  const elements = document.querySelectorAll('.html, .css, .py'); // animate all skill boxes

  function showOnScroll() {
    const triggerBottom = window.innerHeight * 0.85;

    elements.forEach(el => {
      const rect = el.getBoundingClientRect().top;
      if (rect < triggerBottom) {
        el.classList.add('show');
      } else {
        el.classList.remove('show');
      }
    });
  }

  window.addEventListener('scroll', showOnScroll);
  showOnScroll();
});
document.addEventListener("DOMContentLoaded", () => {
  const elements = document.querySelectorAll('.edu-card'); 

  function showOnScroll() {
    const triggerBottom = window.innerHeight * 0.85;

    elements.forEach(el => {
      const rect = el.getBoundingClientRect().top;
      if (rect < triggerBottom) {
        el.classList.add('show');
      } else {
        el.classList.remove('show');
      }
    });
  }

  window.addEventListener('scroll', showOnScroll);
  showOnScroll();
});



function handleNav() {
    const navbar = document.querySelector(".nav-right");
    const currentDisplay = window.getComputedStyle(navbar).display;

    if (currentDisplay === "none") {
        navbar.style.display = "block"; 
        navbar.style.transition = "0.2s" 
    } else {
        navbar.style.display = "none";
    }
  }
function handleTop() {
  const top = document.querySelector(".top");

  if (window.scrollY > 200) {
    top.style.display = "flex";
  } else {
    top.style.display = "none";
  }
}

window.addEventListener("scroll", handleTop);

