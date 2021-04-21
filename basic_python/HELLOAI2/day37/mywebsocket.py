from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__, static_url_path="", static_folder="static")
app.config['SECRET_KEY'] = '1234'
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('session.html')

def myReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('to_server')
def to_server(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('to_client', json, callback=myReceived)
    #내가 보낸걸 다시 돌려주는 방식 : 에코서버

if __name__ == '__main__':
    socketio.run(app, host = "0.0.0.0",port=9999)
                    #host 어느 아이피에서든지 접근을 할 수 있게 도와주는 친구 