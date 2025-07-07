/** @format */

// Initialize tooltips
document.addEventListener("DOMContentLoaded", function () {
  // Enable Bootstrap tooltips
  var tooltipTriggerList = [].slice.call(
    document.querySelectorAll('[data-bs-toggle="tooltip"]')
  );
  var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });

  // Cookie consent functionality
  const cookieConsent = document.querySelector(".cookie-consent");
  const cookieAccept = document.querySelector(".btn-accept");
  const cookieSettings = document.querySelector(".btn-settings");

  // Check if user has already consented
  if (!localStorage.getItem("cookieConsent")) {
    setTimeout(() => {
      cookieConsent.classList.add("active");
    }, 2000);
  }

  // Handle accept button
  if (cookieAccept) {
    cookieAccept.addEventListener("click", function () {
      localStorage.setItem("cookieConsent", "accepted");
      cookieConsent.classList.remove("active");
    });
  }

  // Handle settings button
  if (cookieSettings) {
    cookieSettings.addEventListener("click", function () {
      // Implement your cookie settings modal here
      alert("Cookie settings would open here");
    });
  }

  // Scroll to top button
  const scrollTopBtn = document.querySelector(".scroll-top");
  if (scrollTopBtn) {
    window.addEventListener("scroll", function () {
      if (window.pageYOffset > 300) {
        scrollTopBtn.style.display = "block";
      } else {
        scrollTopBtn.style.display = "none";
      }
    });

    scrollTopBtn.addEventListener("click", function () {
      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });
    });
  }

  // Mobile menu toggle
  const mobileMenuBtn = document.querySelector(".mobile-menu-btn");
  const mobileMenu = document.querySelector(".mobile-menu");

  if (mobileMenuBtn && mobileMenu) {
    mobileMenuBtn.addEventListener("click", function () {
      mobileMenu.classList.toggle("show");
    });
  }
});
