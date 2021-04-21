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

@app.route('/download', methods = ['GET', 'POST'])
def download():
    file_name = f"static/upload/y.png"
    return send_file(file_name,
                     mimetype='image/png', #다운받는 파일의 타입 설정 
                     attachment_filename='downloady.png',# 다운받아지는 파일 이름. 
                     as_attachment=True)


        
if __name__ == "__main__":
    app.run(debug=True)
#   app.run(host='localhost', port=5000)



