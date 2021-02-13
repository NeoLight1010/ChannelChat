const roomName = JSON.parse(document.getElementById('room-name').textContent);

const chatSocket = new WebSocket(
    'ws://' +
    window.location.host +
    '/ws/chat/' +
    roomName +
    '/'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    console.log(data);
    document.querySelector('#tester-div').innerHTML = data.tester;
    document.querySelector("#chat-text").value += data.chatMessage + "\n";
};

document.querySelector("#send-message-btn").onclick = function (e) {
    const messageInputDom = document.querySelector('#message-input');
    const message = messageInputDom.value;

    console.log("Sending: " + message)

    chatSocket.send(JSON.stringify({
        'chatMessage': message,
    }));
    messageInputDom.value = '';
};