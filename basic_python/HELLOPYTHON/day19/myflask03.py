from flask import Flask
from flask.templating import render_template


app = Flask(__name__)

@app.route("/render")    #url-mapping
def render():
    list = ["홍길동","전우치","이순신"]
    return render_template('index.html', list = list, str="대한민국위인들")

if __name__ == "__main__":
    app.run(debug=True)
#   app.run(host='localhost', port=5000)




