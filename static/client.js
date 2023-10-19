document.addEventListener('DOMContentLoaded', function() {
    var socket = io.connect('http://' + document.domain + ':' + location.port, { transports: ['websocket'] });


    socket.on('connect', function() {
        console.log('Connected');
    });

    socket.on('request_received', function(data) {
        var requestDiv = document.getElementById('request_data');
        requestDiv.innerHTML = 'Request Data: ' + JSON.stringify(data);
    });

    socket.on('response_received', function(data) {
        var responseDiv = document.getElementById('response_data');
        responseDiv.innerHTML = 'Response Data: ' + JSON.stringify(data);
    });
});
