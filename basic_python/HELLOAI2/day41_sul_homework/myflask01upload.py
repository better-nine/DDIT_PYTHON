import os
from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__, static_url_path="", static_folder="static")

@app.route("/")    #url-mapping
@app.route("/upload", methods = ['POST'])    #url-mapping
def upload():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join('D:/workspace_python/HELLOAI2/day41/static/upload', filename))
    
    return render_template('upload.html')

#@app.route('/upload_file', methods = ['GET', 'POST'])
#def upload_file():
#     file = request.files['file']   
#     file.save(secure_filename(file.filename))

 

