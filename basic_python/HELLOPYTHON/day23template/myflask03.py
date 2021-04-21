from flask import Flask
from flask.templating import render_template


app = Flask(__name__, static_url_path="", static_folder="static")


@app.route("/suser")  
def suser(): 
    return render_template('suser.html' )

@app.route("/survey")  
def survey(): 
    return render_template('survey.html' )

@app.route("/detail")  
def detail(): 
    return render_template('detail.html' )

if __name__ == "__main__":
    app.run(debug=True) 




