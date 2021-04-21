from flask import Flask
app = Flask(__name__)

@app.route("/hello")    #url-mapping
def hello():
    return "Hello Flasksksasdasdasdksksksksk!"

if __name__ == "__main__":
    app.run(debug=True)
#   app.run(host='localhost', port=5000)