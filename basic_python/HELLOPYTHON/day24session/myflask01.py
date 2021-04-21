from flask import Flask, session,escape, app
from anaconda_navigator.utils.py3compat import request
from datetime import timedelta


app = Flask(__name__, static_url_path="", static_folder="static")


#세션키
app.secret_key = b'asdasd'
 
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1)
    
    
     
@app.route("/in")    #url-mapping
def session_in():
    session['user_id'] = "S0001"
    return "session_in  !"

@app.route("/del")    #url-mapping
def session_del():
    session.pop("user_id", None)
    # session.clear()
    return "session_del  !"

@app.route("/show")    #url-mapping
def session_show():
    user_id =""
    
    try:
        user_id = str(escape(session["user_id"]))
    except : 
        pass
    
    return "session_show : "+user_id
 


if __name__ == "__main__":
    app.run(debug=True)
#   app.run(host='localhost', port=5000)