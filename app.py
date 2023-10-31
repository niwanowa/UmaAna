from flask import Flask, request, render_template
from flask_socketio import SocketIO
import msgpack
import struct

app = Flask(__name__)
socketio = SocketIO(app)

# Load configuration from config.json file
app.config.from_pyfile('config.cfg')
print(app.config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notify/request', methods=['POST'])
def notify_request():
    msgpack_data = request.data
    json_data = unpack_request_data(msgpack_data)
    print(json_data)
    print(type(json_data))
    socketio.emit('request_received', json_data)
    return 'Request Received', 200

@app.route('/notify/response', methods=['POST'])
def notify_response():
    msgpack_data = request.data
    json_data = msgpack.unpackb(msgpack_data, raw=False)
    socketio.emit('response_received', json_data)
    return 'Response Received', 200

def unpack_request_data(msgpack_data):
    # フォーマットに基づいてデータを解析
    offset, = struct.unpack('<I', msgpack_data[:4])
    fixed_data = msgpack_data[4:56]
    variable_data = msgpack_data[56:170]

    # 残りの部分はmsgpack形式のデータとして扱う
    msgpack_msg = msgpack_data[4+offset:]

    # msgpackデータをデコード
    json_data = msgpack.unpackb(msgpack_msg, raw=False)

    return json_data


if __name__ == '__main__':
    socketio.run(app, host=app.config['HOST'], port=app.config['PORT'])
