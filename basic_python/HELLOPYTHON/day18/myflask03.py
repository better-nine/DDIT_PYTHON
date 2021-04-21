from flask import Flask
from flask.templating import render_template


app = Flask(__name__)

@app.route("/render")    #url-mapping
def render():
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
#   app.run(host='localhost', port=5000)




