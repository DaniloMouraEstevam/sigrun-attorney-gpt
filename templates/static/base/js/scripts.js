/*!
* Start Bootstrap - Simple Sidebar v6.0.6 (https://startbootstrap.com/template/simple-sidebar)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-simple-sidebar/blob/master/LICENSE)
*/
 
// Scripts v0.0.0

// Encapsulate code in a function to limit the scope of variables
(function () {
    let form = document.querySelector('#question_form');
    let textarea = document.querySelector('#input_value');
    let chat_container = document.querySelector('.chat-container');
    let isFirstMessage = true;
    let currentChatMessageId = null;
    let sidebarToggle = document.body.querySelector('#sidebarToggle');
    let submitBtn = document.getElementById('submit-btn');
    let fileInput = document.getElementById('file_input');
    let imageInput = document.getElementById('image_input');
    let csrftoken;

    // Event Listener for DOMContentLoaded
    document.addEventListener('DOMContentLoaded', function () {
        initializeTooltips();
        initializeSidebarToggle();
        initializeTextarea();
        initializeFileInputEvents();
        initializeNewChatButton();
        initializeCookieFunctions();
        initializeSubmitButton();
        initializeMessageLinkEvents();
        initializeToggleIcon();
    });

    // Function to initialize Bootstrap tooltips
    function initializeTooltips() {
        const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-toggle="tooltip"]'));
        tooltipTriggerList.forEach(function (tooltipTriggerEl) {
            new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }

    // Function to initialize the sidebar toggle
    function initializeSidebarToggle() {
        if (sidebarToggle) {
            sidebarToggle.addEventListener('click', toggleSidebar);
        }
    }

    // Function to toggle the sidebar
    function toggleSidebar(event) {
        event.preventDefault();
        document.body.classList.toggle('sb-sidenav-toggled');
        localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        toggleIcon();
    }

    // Inicializar toggle de ícone
    function initializeToggleIcon() {
        const sidebarToggle = document.getElementById('sidebarToggle');
        sidebarToggle.setAttribute('title', 'Esconder sidebar');
        $(sidebarToggle).tooltip();
    }

    // Function to switch icons in sidebar
    function toggleIcon() {
        const icon = document.getElementById("toggleIcon");
        const sidebarToggle = document.getElementById('sidebarToggle');

        // Destruir o tooltip existente
        $(sidebarToggle).tooltip('dispose');
        
        if (icon.classList.contains("bi-chevron-left")) {
            icon.classList.replace("bi-chevron-left", "bi-chevron-right");
            sidebarToggle.setAttribute('title', 'Mostrar sidebar');
        } else {
            icon.classList.replace("bi-chevron-right", "bi-chevron-left");
            sidebarToggle.setAttribute('title', 'Esconder sidebar');
        }
        // Inicializar um novo tooltip
        $(sidebarToggle).tooltip();
    }

    // Função para exibir botões em histórico
    window.showButtons = function (messageDiv) {
        const buttons = messageDiv.querySelectorAll('.btn-edit, .btn-delete');
        buttons.forEach(button => button.classList.add('visible'));
    }

    // Função para ocultar botões em histórico
    window.hideButtons = function (messageDiv) {
        const buttons = messageDiv.querySelectorAll('.btn-edit, .btn-delete');
        buttons.forEach(button => button.classList.remove('visible'));
    }






})();