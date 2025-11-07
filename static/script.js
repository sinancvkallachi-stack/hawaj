const slides = document.querySelectorAll('.banner-slide');
    const leftArrow = document.querySelector('.arrow-left');
    const rightArrow = document.querySelector('.arrow-right');
    let currentIndex = 0;

    function updateSlides() {
      const isMobile = window.innerWidth <= 768;
      slides.forEach((slide, index) => {
        slide.style.backgroundImage = `url(${isMobile ? slide.dataset.mobile : slide.dataset.desktop})`;
        slide.classList.toggle('active', index === currentIndex);

        // Reset animation
        const h1 = slide.querySelector('h1');
        const p = slide.querySelector('p');
        if (index === currentIndex) {
          h1.style.animation = 'none';
          p.style.animation = 'none';
          void h1.offsetWidth; // restart animation
          void p.offsetWidth;
          h1.style.animation = 'slideUp 1s forwards';
          p.style.animation = 'slideUp 1s 0.3s forwards';
        }
      });
    }

    leftArrow.addEventListener('click', () => {
      currentIndex = (currentIndex - 1 + slides.length) % slides.length;
      updateSlides();
    });

    rightArrow.addEventListener('click', () => {
      currentIndex = (currentIndex + 1) % slides.length;
      updateSlides();
    });

    window.addEventListener('resize', updateSlides);

    // Auto slide every 5 seconds
    setInterval(() => {
      currentIndex = (currentIndex + 1) % slides.length;
      updateSlides();
    }, 5000);

    updateSlides();

    
 // Shrink Navbar on Scroll
  window.addEventListener('scroll', function() {
    const navbar = document.getElementById('navbar');
    if (window.scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  });

  