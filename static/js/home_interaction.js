// static/js/home_interaction.js
document.addEventListener('DOMContentLoaded', function() {
    // Select all buttons
    const buttons = document.querySelectorAll('button');

    // Loop through each button and add event listeners for 'mouseover' and 'mouseout'
    buttons.forEach(function(button) {
        button.addEventListener('mouseover', function() {
            // Change background color to a darker shade on hover
            this.style.backgroundColor = '#367c39'; // Example darker green
        });

        button.addEventListener('mouseout', function() {
            // Revert to the original color
            this.style.backgroundColor = '#4CAF50'; // Original green
        });

        // Optional: Add a click effect
        button.addEventListener('mousedown', function() {
            this.style.transform = 'scale(0.95)'; // Compress button slightly on click
        });

        button.addEventListener('mouseup', function() {
            this.style.transform = 'scale(1.0)'; // Return to normal scale
        });
    });
});
