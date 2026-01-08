// Initialize driver with fallback for different build versions
const driver = window.driver?.js?.driver || window.driver;

const desktopSteps = [
    { element: '.navbar-brand', popover: { title: 'Welcome to TrackMyRupee!', description: 'This is your personal finance dashboard. Let\'s take a quick tour to verify everything is set up correctly.', side: "bottom", align: 'start' } },
    { element: '.bi-moon-stars-fill, .bi-sun-fill', popover: { title: 'Theme Toggle', description: 'Switch between Dark and Light modes here. The app adapts to your system preference by default.', side: "bottom", align: 'end' } },
    { element: '.col-md-3:nth-child(1)', popover: { title: 'Income Overview', description: 'Track your total income here. Compare it with last month to see your growth.', side: "bottom", align: 'start' } },
    { element: '.col-md-3:nth-child(2)', popover: { title: 'Expense Tracking', description: 'Keep an eye on your spending. We highlight if you\'re spending more than last month.', side: "bottom", align: 'start' } },
    { element: '.col-md-4:nth-child(2)', popover: { title: 'Budget Management', description: 'Visual bars show how much of your budget you\'ve used. Set limits in Settings.', side: "top", align: 'start' } },
    { element: '#nav-expenses', popover: { title: 'Detailed List', description: 'View, edit, or delete individual transactions here.', side: "bottom", align: 'start' } },
    { element: '#nav-settings', popover: { title: 'Settings', description: 'Manage Categories, Budgets, and Currency preferences here.', side: "bottom", align: 'start' } },
];

const mobileSteps = [
    { element: '.navbar-brand', popover: { title: 'Welcome!', description: 'TrackMyRupee helps you manage money on the go.', side: "bottom", align: 'start' } },
    { element: '.navbar-toggler', popover: { title: 'Menu', description: 'Tap here to access Settings, Dark Mode, and Logout.', side: "bottom", align: 'end' } },
    { element: '.col-6:nth-child(1)', popover: { title: 'Income', description: 'Your total income summary.', side: "bottom", align: 'center' } },
    { element: '.col-6:nth-child(2)', popover: { title: 'Expenses', description: 'Your total expenses.', side: "bottom", align: 'center' } },
    { element: '#mobile-fab', popover: { title: 'Quick Actions', description: 'Tap the + button to instantly record a new Transaction.', side: "top", align: 'end' } },
];

const isMobile = window.innerWidth < 768; // Bootstrap md breakpoint

const tourDriver = driver({
    animate: true,
    showProgress: true,
    steps: isMobile ? mobileSteps : desktopSteps,
    onDestroyStarted: () => {
        markTutorialComplete();
        tourDriver.destroy();
    },
});

function startTour() {
    tourDriver.drive();
}

function markTutorialComplete() {
    // Only mark complete if we are logged in (indicated by the presence of the tutorial complete URL)
    if (window.tutorialCompleteUrl) {
        fetch(window.tutorialCompleteUrl, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Content-Type': 'application/json'
            }
        }).then(response => {
            if (response.ok) {
                console.log('Tutorial marked as complete');
            }
        }).catch(err => console.error(err));
    }
}

// CSRF Token Helper
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
