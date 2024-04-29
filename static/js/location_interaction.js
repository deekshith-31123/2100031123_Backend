// static/js/location_interaction.js
document.addEventListener('DOMContentLoaded', function () {
    const submitBtn = document.querySelector('.submit-btn');
    submitBtn.addEventListener('mouseover', function () {
        this.style.backgroundColor = '#1b6f5f'; // Darker tone on hover
    });
    submitBtn.addEventListener('mouseout', function () {
        this.style.backgroundColor = '#2a9d8f'; // Original color on mouse out
    });
});
