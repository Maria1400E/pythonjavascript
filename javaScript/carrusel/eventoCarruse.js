const slides = document.querySelectorAll(".slide");
const prevButton = document.getElementById("prevBtn");
const nextButton = document.getElementById("nextBtn");
let currentIndex = 0;

function showSlide(index) {
  slides.forEach((slide, i) => {
    if (i === index) {
      slide.style.display = "block";
    } else {
      slide.style.display = "none";
    }
  });
}

prevButton.addEventListener("click", () => {
  currentIndex = (currentIndex - 1 + slides.length) % slides.length;
  showSlide(currentIndex);
});

nextButton.addEventListener("click", () => {
  currentIndex = (currentIndex + 1) % slides.length;
  showSlide(currentIndex);
});

// Mostrar el primer slide al cargar la página
showSlide(currentIndex);