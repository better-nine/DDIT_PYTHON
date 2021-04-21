from flask import Flask,request
from flask.templating import render_template
import cx_Oracle

app = Flask(__name__, static_url_path="", static_folder="static")

@app.route("/") 
@app.route("/sample") 
def sample():
    
    list =[]
    list.append({'survey_id':'1','s_seq':'1', 'question':'맛식?', 'a1':'맥날', 'a2':'맥날', 'a3':'맥날', 'a4':'맥날','c1':1,'c2':1,'c3':1,'c4':1})
    list.append({'survey_id':'1','s_seq':'2', 'question':'맛식2?', 'a1':'맥날', 'a2':'맥날', 'a3':'맥날', 'a4':'맥날','c1':1,'c2':1,'c3':1,'c4':1})
    
    return render_template('sample.html', list=list, enumerate=enumerate)

@app.route("/sample2") 
def sample2():
    
    
    list =[]
    list.append({'survey_id':'1','s_seq':'1', 'question':'맛식?', 'a1':'맥날', 'a2':'맥날', 'a3':'맥날', 'a4':'맥날','c1':1,'c2':1,'c3':1,'c4':1})
    list.append({'survey_id':'1','s_seq':'2', 'question':'맛식2?', 'a1':'맥날', 'a2':'맥날', 'a3':'맥날', 'a4':'맥날','c1':1,'c2':1,'c3':1,'c4':1})
    
    return render_template('sample2.html', list=list, enumerate=enumerate)


if __name__ == "__main__":
    app.run(debug=True)
    
