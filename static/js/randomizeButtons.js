document.addEventListener("DOMContentLoaded", function() {
    const container = document.getElementById('choice-container');
    if (container) { // Check if container exists to avoid errors on pages without it
        const buttons = Array.from(container.children); // Get all buttons as an array
        buttons.sort(() => Math.random() - 0.5); // Randomize their order
        buttons.forEach(button => container.appendChild(button)); // Re-append in new order
    }
});