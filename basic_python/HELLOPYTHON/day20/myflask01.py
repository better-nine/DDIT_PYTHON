from flask import Flask, request, jsonify, render_template

app = Flask(__name__, static_url_path='', static_folder='static')
 
@app.route("/ajax", methods=['POST'])    #url-mapping
def ajax(): 
    col01 = request.form['col01']
    col02 = request.form['col02']
    print(col01,col02)
    
    return jsonify(msg='ok')

if __name__ == "__main__":
    app.run(debug=True)
    