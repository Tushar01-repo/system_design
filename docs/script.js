// Toggle sidebar dropdown
function toggleSidebar(button, itemsId) {
    const items = document.getElementById(itemsId);
    const arrow = button.querySelector('.arrow');
    
    // Close other open dropdowns
    document.querySelectorAll('.sidebar-items').forEach(item => {
        if (item.id !== itemsId) {
            item.classList.add('hidden');
        }
    });
    
    // Toggle current dropdown
    items.classList.toggle('hidden');
    arrow.style.transform = items.classList.contains('hidden') ? 'rotate(0deg)' : 'rotate(90deg)';
}

// Navigation smooth scroll
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        
        // Remove active class from all links
        document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
        
        // Add active class to clicked link
        this.classList.add('active');
        
        // Scroll to section
        const targetId = this.getAttribute('href');
        const targetSection = document.querySelector(targetId);
        if (targetSection) {
            targetSection.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Sidebar item smooth scroll
document.querySelectorAll('.sidebar-item').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        
        // Scroll to section
        const targetId = this.getAttribute('href');
        if (targetId && targetId.startsWith('#')) {
            const targetSection = document.querySelector(targetId);
            if (targetSection) {
                targetSection.scrollIntoView({ behavior: 'smooth' });
            }
        }
    });
});

// Set home as active on page load
window.addEventListener('load', function() {
    const navLink = document.querySelector('.nav-link');
    if (navLink) {
        navLink.classList.add('active');
    }
});

// Mobile menu toggle
const sidebarHeader = document.querySelector('.sidebar-header');
if (sidebarHeader) {
    sidebarHeader.addEventListener('click', function() {
        const sidebar = document.querySelector('.sidebar');
        sidebar.classList.toggle('active');
    });
}
