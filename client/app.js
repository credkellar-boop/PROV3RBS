// WebSocket Initialization
const clientId = Math.floor(Math.random() * 1000);
const ws = new WebSocket(`ws://${window.location.host}/ws/${clientId}`);
const chatBox = document.getElementById('chat-box');
const messageInput = document.getElementById('message-input');

ws.onmessage = (event) => {
    const msgElement = document.createElement('p');
    msgElement.textContent = event.data;
    chatBox.appendChild(msgElement);
    chatBox.scrollTop = chatBox.scrollHeight;
};

function sendMessage() {
    const msg = messageInput.value;
    if(msg.trim() !== "") {
        ws.send(msg);
        messageInput.value = '';
    }
}

messageInput.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }
});
