/*!
* Start Bootstrap - Simple Sidebar v6.0.6 (https://startbootstrap.com/template/simple-sidebar)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-simple-sidebar/blob/master/LICENSE)
*/
// 
// Scripts
// 

// Simple Sidebar v6.0.6
window.addEventListener('DOMContentLoaded', event => {
    // Ativar tooltips usando Bootstrap
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});


// Adiciona lógica para alternar entre os ícones quando o botão for pressionado
function toggleIcon() {
    var icon = document.getElementById("toggleIcon");


    if (icon.classList.contains("bi-chevron-left")) {
        icon.classList.remove("bi-chevron-left");
        icon.classList.add("bi-chevron-right");
        document.getElementById('sidebarToggle').setAttribute('title', 'Mostrar sidebar');
    } else {
        icon.classList.remove("bi-chevron-right");
        icon.classList.add("bi-chevron-left");
        document.getElementById('sidebarToggle').setAttribute('title', 'Esconder sidebar');
    }
}


// Mostrar / Ocultar ícones na caixa de histórico
function showButtons(messageDiv) {
    var buttons = messageDiv.querySelectorAll('.btn-edit, .btn-delete');
    buttons.forEach(function (button) {
        button.style.visibility = 'visible';
        button.style.backgroundColor = '#edf2f4';
    });
}


function hideButtons(messageDiv) {
    var buttons = messageDiv.querySelectorAll('.btn-edit, .btn-delete');
    buttons.forEach(function (button) {
        button.style.visibility = 'hidden';
    });
}


// Ajuste na altura da caixa de perguntas
document.getElementById('input_value').addEventListener('input', function () {
    this.style.height = '';

    if (this.scrollHeight <= 150) {
        this.style.height = this.scrollHeight + 'px';
        document.documentElement.style.setProperty('--submit-form-height', this.style.height);
        document.querySelector('.container-fluid-2').style.height = 'calc(80vh - ' + this.style.height + ' + 38px)';
    } else {
        this.style.height = '150px';
        document.documentElement.style.setProperty('--submit-form-height', this.style.height);
        document.querySelector('.container-fluid-2').style.height = 'calc(80vh - ' + this.style.height + ' + 38px)';
    }

    if (this.value === '') {
        this.style.height = '40px';
        document.documentElement.style.setProperty('--submit-form-height', '60px');
        document.querySelector('.container-fluid-2').style.height = '80vh';
    }
});


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


// Bloco responsável pelo envio de mensagem e atualização do chat
let form = document.querySelector('#question_form')
let textarea = document.querySelector('#input_value')
let chat_container = document.querySelector('.chat-container')
let isFirstMessage = true;

form.addEventListener('submit', submitForm)

async function postJSON(data) {
    const url = '/chat/get-question/'

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify(data),
        });

        const result = await response.json();
        chat_container.innerHTML +=
            `<div class="d-flex flex-row justify-content-end mb-1">
                    <div class="mw-75">
                        <p class="small me-3 mb-3 rounded-3 user-chat">${result.msg}</p>
                    </div>
                    <img src="${userFotoPerfilUrl}" class="rounded-circle" style="width: 45px; height: 100%;">
                </div>
                <div class="d-flex flex-row justify-content-start mb-1">
                    <img src="${botImageUrl}" class="rounded-circle" style="width: 45px; height: 100%;">
                    <div class="mw-75">
                        <p class="small ms-3 mb-3 rounded-3 bot-chat">${result.res}</p>
                    </div>
                </div>`;

        textarea.value = ''

        console.log('Sucesso', result);
    } catch (error) {
        console.error("Erro:", error);
    }
}

// Bloco para atualização da caixa de histórico na sidebar
function updateHistoryBlock(message) {
    let todayBlock = document.getElementById('t-block');

    if (todayBlock) {
        let todayList = todayBlock.querySelector('ul');
        let todayMessages = todayList.querySelectorAll('li');

        let messageExists = Array.from(todayMessages).some(function (li) {
            return li.querySelector('.history a').textContent === message;
        });

        if (messageExists) {
            // A mensagem já existe, não é necessário adicionar uma nova
            console.log('Mensagem já existe:', message);
        } else {
            // A mensagem não existe, adicione uma nova
            todayList.innerHTML += `
                    <li>
                        <div class="history" onmouseover="showButtons(this)" onmouseout="hideButtons(this)">
                            <a href="#">${message}</a>
                            <button class="btn-edit"><i class="fa-solid fa-pencil"></i></button>
                            <button class="btn-delete"><i class="fa-solid fa-trash"></i></button>
                        </div>
                    </li>`;
        }
    }
}


// Bloco para ativação dos eventos
function submitForm(e) {
    e.preventDefault()

    if (isFirstMessage) {
        updateHistoryBlock(textarea.value);
    }

    let message = textarea.value;
    const data = { msg: message, is_first_message: isFirstMessage };
    postJSON(data);
    isFirstMessage = false;
}

