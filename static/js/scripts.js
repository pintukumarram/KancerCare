// Card hover glow and sound
document.querySelectorAll(".card").forEach((card) => {
  const audio = new Audio("static/sounds/woosh-effect.mp3");

  card.addEventListener("mouseenter", () => {
    card.style.boxShadow = "0 10px 30px rgba(255, 87, 34, 0.4)";
    audio.currentTime = 0;
    audio.play();
  });

  card.addEventListener("mouseleave", () => {
    card.style.boxShadow = "5px 5px 15px rgba(0, 0, 0, 0.4), -5px -5px 15px rgba(255, 255, 255, 0.1)";
    audio.pause();
    audio.currentTime = 0;
  });
});

// Pause/resume carousel on hover
document.addEventListener("DOMContentLoaded", () => {
  const carouselTrack = document.querySelector(".carousel-track");
  carouselTrack.addEventListener("mouseenter", () => {
    carouselTrack.style.animationPlayState = "paused";
  });
  carouselTrack.addEventListener("mouseleave", () => {
    carouselTrack.style.animationPlayState = "running";
  });
});

// Smooth scroll & active navbar highlight
document.addEventListener("DOMContentLoaded", () => {
  const navItems = document.querySelectorAll(".nav-item");
  const sections = document.querySelectorAll("section");

  navItems.forEach((item) => {
    item.addEventListener("click", (e) => {
      e.preventDefault();
      const target = document.querySelector(item.getAttribute("href"));
      window.scrollTo({
        top: target.offsetTop - 60,
        behavior: "smooth",
      });
    });
  });

  window.addEventListener("scroll", () => {
    let scrollY = window.scrollY;
    sections.forEach((section, index) => {
      if (
        scrollY >= section.offsetTop - 70 &&
        scrollY < section.offsetTop + section.offsetHeight
      ) {
        navItems.forEach((item) => item.classList.remove("active"));
        navItems[index].classList.add("active");
      }
    });
  });
});

// Button click sound
document.addEventListener("DOMContentLoaded", () => {
  const predictButton = document.querySelector(".submit-button");
  const clickSound = new Audio("/static/sounds/click.wav");

  predictButton.addEventListener("click", () => {
    clickSound.play();
  });
});

particlesJS("particles-js", {
  particles: {
    number: { value: 80 },
    color: { value: "#00bcd4" },
    shape: { type: "circle" },
    opacity: { value: 0.3 },
    size: { value: 4 },
    line_linked: {
      enable: true,
      distance: 150,
      color: "#00bcd4",
      opacity: 0.2,
      width: 1
    },
    move: {
      enable: true,
      speed: 2,
      direction: "none",
      out_mode: "bounce"
    }
  },
  interactivity: {
    detect_on: "canvas",
    events: {
      onhover: { enable: true, mode: "repulse" }
    }
  }
});
