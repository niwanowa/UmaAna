from flask import Flask, request, render_template
from flask_socketio import SocketIO
import msgpack

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notify/request', methods=['POST'])
def notify_request():
    msgpack_data = request.data
    json_data = msgpack.unpackb(msgpack_data, raw=False)
    print(json_data)
    socketio.emit('request_received', json_data)
    return 'Request Received', 200

@app.route('/notify/response', methods=['POST'])
def notify_response():
    msgpack_data = request.data
    json_data = msgpack.unpackb(msgpack_data, raw=False)
    print(json_data)
    socketio.emit('response_received', json_data)
    return 'Response Received', 200

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=4693)
