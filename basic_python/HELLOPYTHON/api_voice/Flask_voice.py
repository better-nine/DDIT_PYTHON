from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO

app = Flask(__name__, static_url_path="", static_folder="static")
app.config['SECRET_KEY'] = '1234'
socketio = SocketIO(app)

@app.route('/')
@app.route('/test')
def test():
    return render_template('test.html')


def voice():
    import requests
    import json
    import speech_recognition as sr
    
    url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
    rest_api_key = 'adb174ed9071842964dcd029e2ea63d2'
    header = {
    "Content-Type": "application/octet-stream",
    "X-DSS-Service": "DICTATION",
    "Authorization": "KakaoAK " + rest_api_key,
    }
    
    rec = sr.Recognizer()
    
    
    









if __name__ == "__main__":
    socketio.run(app, host = "0.0.0.0",port=9999)