document.addEventListener('DOMContentLoaded', function() {
    var socket = io.connect('http://' + document.domain + ':' + location.port, { transports: ['websocket'] });


    socket.on('connect', function() {
        console.log('Connected');
    });

    socket.on('request_received', function(data) {
        var requestDiv = document.getElementById('request_data');
        requestDiv.innerHTML = JSON.stringify(data, null, "\t");
    });

    socket.on('response_received', function(data) {
        var responseDiv = document.getElementById('response_data');
        responseDiv.innerHTML = JSON.stringify(data, null, "\t");
    });
});
