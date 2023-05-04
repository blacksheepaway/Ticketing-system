document.addEventListener('DOMContentLoaded', function() {
    const header = document.querySelector('header');
    header.style.backgroundColor = '#222';
    
    header.addEventListener('mouseover', function() {
      header.style.backgroundColor = '#35424a';
    });
  
    header.addEventListener('mouseout', function() {
      header.style.backgroundColor = '#222';
    });
  });
  