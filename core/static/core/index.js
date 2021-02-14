document.querySelector('#enter-room').onclick = function (e) {
    console.log("clicked me");
    const roomInputDom = document.querySelector('#room-name');
    const roomName = roomInputDom.value;

    window.location.href = './chat/' + roomName;
    roomInputDom.value = "";
};
