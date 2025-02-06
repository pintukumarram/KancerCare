document.querySelectorAll(".card").forEach((card) => {
  card.addEventListener("mouseenter", () => {
    card.style.boxShadow = "0 10px 30px rgba(255, 87, 34, 0.4)";
  });
  card.addEventListener("mouseleave", () => {
    card.style.boxShadow =
      "5px 5px 15px rgba(0, 0, 0, 0.4), -5px -5px 15px rgba(255, 255, 255, 0.1)";
  });
});

document.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll(".card");
  const audio = new Audio("static/sounds/woosh-effect.mp3"); // Ensure this path is correct

  cards.forEach((card) => {
    card.addEventListener("mouseenter", () => {
      // Play the sound when hovering
      audio.currentTime = 0; // Reset to the start
      audio.play();
    });

    card.addEventListener("mouseleave", () => {
      // Optionally, stop the sound when leaving the card
      audio.pause();
      audio.currentTime = 0; // Reset for the next hover
    });
  });
});

// JavaScript for pause on hover effect
document.addEventListener("DOMContentLoaded", () => {
  const carouselTrack = document.querySelector(".carousel-track");
  let isPaused = false;

  // Pause animation on hover
  carouselTrack.addEventListener("mouseenter", () => {
    isPaused = true;
    carouselTrack.style.animationPlayState = "paused";
  });

  // Resume animation when not hovering
  carouselTrack.addEventListener("mouseleave", () => {
    isPaused = false;
    carouselTrack.style.animationPlayState = "running";
  });
});

// Smooth Scroll and Active Link
document.addEventListener("DOMContentLoaded", () => {
  const navItems = document.querySelectorAll(".nav-item");
  const sections = document.querySelectorAll("section");

  // Smooth Scroll
  navItems.forEach((item) => {
    item.addEventListener("click", (e) => {
      e.preventDefault();
      const targetSection = document.querySelector(item.getAttribute("href"));
      window.scrollTo({
        top: targetSection.offsetTop - 60, // Offset for navbar height
        behavior: "smooth",
      });
    });
  });

  // Highlight Active Link
  window.addEventListener("scroll", () => {
    let scrollPosition = window.scrollY;
    sections.forEach((section, index) => {
      if (
        scrollPosition >= section.offsetTop - 70 &&
        scrollPosition < section.offsetTop + section.offsetHeight
      ) {
        navItems.forEach((item) => item.classList.remove("active"));
        navItems[index].classList.add("active");
      }
    });
  });
});

document.addEventListener("DOMContentLoaded", () => {
  const predictButton = document.querySelector(".submit-button");
  const sound = new Audio("/static/sounds/click.wav");

  predictButton.addEventListener("click", () => {
    sound.play();
  });
});
