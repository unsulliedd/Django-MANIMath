/************** Hide Navbar When Scroll **************/

var firstScrollPosition = window.pageYOffset;                       //Assigns page height to 'firstScrollPosition'
window.onscroll = function () {
    var currentScrollPosition = window.pageYOffset;
    if (firstScrollPosition > currentScrollPosition) {
        document.getElementById("navbar").style.top = "0";      //Shows navbar
    } else {
        document.getElementById("navbar").style.top = "-60px";  //Hides Navbar
    }
    firstScrollPosition = currentScrollPosition;            //Update scroll position
}

/************** Hide Navbar When Scroll **************/


/************** Dark Mode Script **************/

let darkMode = localStorage.getItem('darkMode');    // Check the 'darkMode' value stored in localStorage

const darkModeToggle = document.querySelector('#dark-mode-toggle');
const moonIcon = '<i class="fa-solid fa-moon"></i>';
const sunIcon = '<i class="fa-solid fa-sun"></i>';

const enableDarkMode = () => {
    document.body.classList.remove('lightmode');    // Remove the 'lightmode' class from the body element
    document.body.classList.add('darkmode');        // Add class to the body element
    darkModeToggle.innerHTML = sunIcon;             // Update the icon
    localStorage.setItem('darkMode', 'enabled');    // Update the 'darkMode' value in localStorage
}

const disableDarkMode = () => {
    document.body.classList.remove('darkmode');     // Remove class from the body element
    document.body.classList.add('lightmode');       // Remove the 'lightmode' class from the body element
    darkModeToggle.innerHTML = moonIcon;            // Update the icon
    localStorage.setItem('darkMode', null);         // Update the 'darkMode' value in localStorage
}

const applyTheme = () => {
    const body = document.body;
    if (darkMode === 'enabled') {
        body.classList.add('darkmode');
        darkModeToggle.innerHTML = sunIcon;         // Update the icon
    } else {
        body.classList.remove('darkmode');
        darkModeToggle.innerHTML = moonIcon;        // Update the icon
    }
}

darkModeToggle.addEventListener('click', () => {
    darkMode = localStorage.getItem('darkMode');
    if (darkMode !== 'enabled') {
        enableDarkMode();
    } else {
        disableDarkMode();
    }
});

applyTheme();  // Apply the theme

/************** Dark Mode Script **************/

/************** Loading Spinner **************/
$(document).ready(function () {
    $('#animation-form').submit(function (event) {
        event.preventDefault();

        $('#loading-spinner').show();

        $.ajax({
            type: "POST",
            url: $(this).attr('action'),
            data: $(this).serialize(),
            success: function (response) {
                var videoHtml = response.video_html;

                $('#video-container').html(videoHtml);
                $('#loading-spinner').hide();
                $('#animation-form')[0].reset();

            },
            error: function (xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
                $('#loading-spinner').hide();
            }
        });
    });
});

/************** Loading Spinner **************/