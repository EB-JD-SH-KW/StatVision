/*--    Authors:   			Eric Bridgens | Joshua Dickens | Kyle Willoughby    --*/
/*--    Creation Date:  	August 15, 2024                                     --*/
/*--    Project Name:   	StatVision                                          --*/



// Listen for the DOM content to be fully loaded
document.addEventListener('DOMContentLoaded', () => {

    // Select all <time> elements with a datetime attribute and iterate over them
    document.querySelectorAll('time[datetime]').forEach(el => {

        // Get the datetime attribute (UTC value) from the element
        const utc = el.getAttribute('datetime');

        // If no datetime is provided, exit the function for this element
        if (!utc) return;

        // Create a new Date object using the UTC time
        const dt = new Date(utc);

        // Format the date to show just the hour and minute in AM/PM format and update the element's text
        el.textContent = dt.toLocaleTimeString([], {

            // Use numeric hours
            hour: 'numeric',

            // Ensure minutes are two digits
            minute: '2-digit',

            // Use 12‑hour time format
            hour12: true
        });
    });
  
    // Select the element with class "scoreboard" to implement drag‑scrolling
    const slider = document.querySelector('.scoreboard');

    // If the scoreboard element is not found, exit the script
    if (!slider) return;
  
    // Initialize variables for tracking the drag state and positions
    let isDown = false, startX, scrollLeft;

    // Add an event listener for when the mouse button is pressed down on the scoreboard
    slider.addEventListener('mousedown', e => {

        // Set the dragging flag to true
        isDown = true;

        // Change the cursor style to indicate dragging
        slider.style.cursor = 'grabbing';

        // Calculate the starting X position relative to the scoreboard
        startX = e.pageX - slider.offsetLeft;

        // Record the current horizontal scroll position of the scoreboard
        scrollLeft = slider.scrollLeft;
    });

    // Add an event listener on the document for mouse button release to stop dragging
    document.addEventListener('mouseup', () => {

        // Set the dragging flag to false
        isDown = false;

        // Reset the cursor style back to "grab"
        slider.style.cursor = 'grab';
    });

    // Add an event listener for when the mouse leaves the scoreboard area to stop dragging
    slider.addEventListener('mouseleave', () => {
        
        // Set the dragging flag to false
        isDown = false;

        // Reset the cursor style back to "grab"
        slider.style.cursor = 'grab';
    });

    // Add an event listener for mouse movement over the scoreboard for the drag‑scroll action
    slider.addEventListener('mousemove', e => {

        // If the mouse button isn't held down, do nothing
        if (!isDown) return;

        // Prevent the default behavior (such as text selection)
        e.preventDefault();

        // Calculate the current mouse X position relative to the scoreboard
        const x = e.pageX - slider.offsetLeft;

        // Calculate how far the mouse has moved from the start position, multiplied by a scroll factor (2)
        const walk = (x - startX) * 2;

        // Adjust the scroll position of the scoreboard based on the movement
        slider.scrollLeft = scrollLeft - walk;
    });
});
