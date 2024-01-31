// /*!
// * Start Bootstrap - Simple Sidebar v6.0.6 (https://startbootstrap.com/template/simple-sidebar)
// * Copyright 2013-2023 Start Bootstrap
// * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-simple-sidebar/blob/master/LICENSE)
// */
// // 
// // Scripts v0.0.0
// //

// let form = document.querySelector('#question_form')
// let textarea = document.querySelector('#input_value')
// let chat_container = document.querySelector('.chat-container')
// let isFirstMessage = true;
// let currentChatMessageId = null;

// // Simple Sidebar v6.0.6
// window.addEventListener('DOMContentLoaded', event => {
//     // Ativar tooltips usando Bootstrap
//     var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-toggle="tooltip"]'));
//     var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
//         return new bootstrap.Tooltip(tooltipTriggerEl);
//     });

//     // Toggle the side navigation
//     const sidebarToggle = document.body.querySelector('#sidebarToggle');
//     if (sidebarToggle) {
//         // Uncomment Below to persist sidebar toggle between refreshes
//         // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
//         //     document.body.classList.toggle('sb-sidenav-toggled');
//         // }
//         sidebarToggle.addEventListener('click', event => {
//             event.preventDefault();
//             document.body.classList.toggle('sb-sidenav-toggled');
//             localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
//         });
//     }

// });


// // Habilitar o botão de envio somente no caso de haver mensagem
// document.addEventListener('DOMContentLoaded', function() {
//     var textarea = document.getElementById('input_value');
//     var submitBtn = document.getElementById('submit-btn');

//     function checkTextarea() {
//         submitBtn.disabled = textarea.value.trim() === '';
//     }

//     checkTextarea();

//     textarea.addEventListener('input', function() {
//         checkTextarea();
//     });

//     document.getElementById('question_form').addEventListener('submit', function() {
//         // Desative o botão de envio após o envio da primeira mensagem
//         submitBtn.disabled = true;
//     });
// });


// // Adiciona lógica para alternar entre os ícones quando o botão for pressionado
// function toggleIcon() {
//     var icon = document.getElementById("toggleIcon");


//     if (icon.classList.contains("bi-chevron-left")) {
//         icon.classList.remove("bi-chevron-left");
//         icon.classList.add("bi-chevron-right");
//         document.getElementById('sidebarToggle').setAttribute('title', 'Mostrar sidebar');
//     } else {
//         icon.classList.remove("bi-chevron-right");
//         icon.classList.add("bi-chevron-left");
//         document.getElementById('sidebarToggle').setAttribute('title', 'Esconder sidebar');
//     }
// }


// // Mostrar / Ocultar ícones na caixa de histórico
// function showButtons(messageDiv) {
//     var buttons = messageDiv.querySelectorAll('.btn-edit1, .btn-delete1');
//     buttons.forEach(function (button) {
//         button.style.visibility = 'visible';
//     });
// }

// function hideButtons(messageDiv) {
//     var buttons = messageDiv.querySelectorAll('.btn-edit1, .btn-delete1');
//     buttons.forEach(function (button) {
//         button.style.visibility = 'hidden';
//     });
// }


// // Ajuste na altura da caixa de perguntas
// function adjustContainerHeight() {
//     const inputTextarea = document.getElementById('input_value');
//     const filePreviewContainer = document.getElementById('file-preview-container');
//     const filePreviewContainerHeight = filePreviewContainer.offsetHeight;
//     const isVisible = filePreviewContainer.style.display !== 'none';

//     // Calculate the new height based on textarea content
//     const newHeight = Math.min(inputTextarea.scrollHeight, 150);

//     // Check if textarea is empty
//     if (inputTextarea.value.trim() === '') {
//         inputTextarea.style.height = '40px'; // Set to original height
//     } else {
//         inputTextarea.style.height = newHeight + 'px';
//     }

//     document.documentElement.style.setProperty('--submit-form-height', inputTextarea.style.height);

//     // Adjust container-fluid-2 height considering file-preview-container visibility
//     const containerFluid3Height = `calc(75vh - ${inputTextarea.style.height} + 38px${isVisible ? ` - ${filePreviewContainerHeight}px` : ''})`;
//     document.querySelector('.container-fluid-2').style.height = containerFluid3Height;
// }


// document.getElementById('input_value').addEventListener('input', function () {
//     adjustContainerHeight();
// });


// // Bloco para exibição dos arquivos em anexo
// function updateFilePreview(inputId, previewId) {
//     const fileInput = document.getElementById(inputId);
//     const preview = document.getElementById(previewId);

//     if (fileInput.files.length > 0) {
//         preview.textContent = `Arquivo: ${fileInput.files[0].name}`;
//     } else {
//         preview.textContent = '';
//     }
// }


// document.getElementById('btnFile').addEventListener('click', function () {
//     document.getElementById('file_input').click();
// });

// document.getElementById('btnImage').addEventListener('click', function () {
//     document.getElementById('image_input').click();
// });

// document.getElementById('file_input').addEventListener('change', function () {
//     updateFilePreview('file_input', 'file-preview');
//     document.getElementById('file-preview-container').style.display = 'flex';
//     adjustContainerHeight();
// });

// document.getElementById('image_input').addEventListener('change', function () {
//     updateFilePreview('image_input', 'file-preview');
//     document.getElementById('file-preview-container').style.display = 'flex';
//     adjustContainerHeight();
// });

// document.getElementById('submit-btn').addEventListener('click', function () {
//     document.getElementById('file-preview-container').style.display = 'none';
//     adjustContainerHeight();
// });

// document.getElementById('remove-file').addEventListener('click', function () {
//     document.getElementById('file-preview-container').style.display = 'none';
//     adjustContainerHeight();
//     updateFilePreview('', 'file-preview');
// });


// // Botão para ciar um novo chat
// document.addEventListener('DOMContentLoaded', function () {
//     let newChatBtn = document.getElementById('newChatBtn');

//     newChatBtn.addEventListener('click', function (event) {
//         event.preventDefault();
//         location.reload();
//     });
// });


// // Bloco para recebimento de Cookies
// function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         const cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             const cookie = cookies[i].trim();
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
// const csrftoken = getCookie('csrftoken');


// // Bloco para envio das mensagens
// async function postFormData(formData) {
//     const url = '/chat/get-question/';

//     try {
//         const response = await fetch(url, {
//             method: 'POST',
//             headers: {
//                 'X-CSRFToken': csrftoken
//             },
//             body: formData,
//         });

//         const result = await response.json();
//         chat_container.innerHTML +=
//             `<div class="d-flex flex-row justify-content-end mb-1">
//             <div class="mw-75">
//                 <p class="small me-3 mb-3 rounded-3 user-chat">${result.msg}</p>
//             </div>
//             <img src="${userFotoPerfilUrl}" class="rounded-circle" style="width: 45px; height: 100%;">
//         </div>
//         <div class="d-flex flex-row justify-content-start mb-1">
//             <img src="${botImageUrl}" class="rounded-circle" style="width: 45px; height: 100%;">
//             <div class="mw-75">
//                 <p class="small ms-3 mb-3 rounded-3 bot-chat">${result.res}</p>
//             </div>
//         </div>`;

//         textarea.value = '';

//         return result.first_id;
//     } catch (error) {
//         console.error("Erro:", error);
//     }
// }


// // Bloco para atualização da caixa de histórico na sidebar
// function updateHistoryBlock(message, chat_id) {
//     let todayBlock = document.getElementById('t-block');

//     if (todayBlock) {
//         let todayList = todayBlock.querySelector('ul');
//         let todayMessages = todayList.querySelectorAll('li');

//         let messageExists = Array.from(todayMessages).some(function (li) {
//             return li.querySelector('.history-container a').textContent === message;
//         });

//         if (messageExists) {
//             console.log('Mensagem já existe:', message);
//         } else {
//             let messageId = todayBlock.dataset.id && todayBlock.dataset.id !== "" ? todayBlock.dataset.id : chat_id;
//             let viewMessageUrl = `/chat/view-messages/${messageId}`;

//             todayList.innerHTML +=
//                 `<li>
//                 <div class="history-container" data-id="${messageId}" onmouseover="showButtons(this)" onmouseout="hideButtons(this)">
//                     <a href="${viewMessageUrl}" id="view_messages_${messageId}" class="view_messages_link">
//                         <div class="history">${message}</div>
//                     </a>
//                     <div class="history-buttons">
//                         <button class="btn-edit"><i class="fa-solid fa-pencil"></i></button>
//                         <button class="btn-delete"><i class="fa-solid fa-trash"></i></button>
//                     </div>
//                 </div>
//             </li>`;
//         }
//     }
// }


// // Bloco para renderizar as mensagens do hisórico no chat
// async function renderMessages(chat_message_id) {
//     const url = `/chat/view-messages/${chat_message_id}`;
//     console.log(url)

//     try {
//         const response = await fetch(url);
//         const messages = await response.json();
//         console.log(messages)

//         const chat_container = document.querySelector('.chat-container');
//         chat_container.innerHTML = '';

//         if (Array.isArray(messages)) {
//             messages.forEach(message => {
//                 chat_container.innerHTML +=
//                     `<div class="d-flex flex-row justify-content-end mb-1">
//                     <div class="mw-75">
//                         <p class="small me-3 mb-3 rounded-3 user-chat">${message.user_question}</p>
//                     </div>
//                     <img src="${userFotoPerfilUrl}" class="rounded-circle" style="width: 45px; height: 100%;">
//                 </div>
//                 <div class="d-flex flex-row justify-content-start mb-1">
//                     <img src="${botImageUrl}" class="rounded-circle" style="width: 45px; height: 100%;">
//                     <div class="mw-75">
//                         <p class="small ms-3 mb-3 rounded-3 bot-chat">${message.bot_response}</p>
//                     </div>
//                 </div>`;
//             });
//         } else {
//             console.error('A resposta não é um array de mensagens:', messages);
//         }


//         currentChatMessageId = chat_message_id;

//     } catch (error) {
//         console.error("Erro:", error);
//     }
// }


// document.querySelectorAll('.view_messages_link').forEach(link => {
//     link.addEventListener('click', function (event) {
//         event.preventDefault();
//         const chat_message_id = this.getAttribute('id').split('_')[2];
//         renderMessages(chat_message_id);
//     });
// });


// form.addEventListener('submit', submitForm)


// // Bloco para ativação dos eventos
// async function submitForm(e) {
//     e.preventDefault();

//     let message = textarea.value;
//     let fileInput = document.getElementById('file_input');
//     let imageInput = document.getElementById('image_input');

//     const data = new FormData();
//     data.append('msg', message);
//     data.append('is_first_message', currentChatMessageId ? false : isFirstMessage);
//     data.append('chat_message_id', currentChatMessageId || undefined);
//     data.append('document', fileInput.files[0] || null);
//     data.append('image', imageInput.files[0] || null);

//     try {
//         const chatId = await postFormData(data);

//         if (isFirstMessage) {
//             updateHistoryBlock(message, chatId);
//         }

//         isFirstMessage = false;
//         currentChatMessageId = null;

//         await renderMessages(chatId);

//         updateFilePreview('', 'file-preview');
//         document.getElementById('file_input').value = '';
//         document.getElementById('image_input').value = '';

//     } catch (error) {
//         console.error("Error:", error);
//     }
// }