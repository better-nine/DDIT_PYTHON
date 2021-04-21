from flask import Flask,render_template, jsonify, request
import cx_Oracle
from day21.mydao import MyDao

app = Flask(__name__, static_url_path="", static_folder="static")

@app.route('/sample')
def render():
    list = MyDao().myselect()
    return render_template('sample.html',list=list)

@app.route('/sample_ins.ajax', methods=['POST'])
def sample_ins_ajax():
    col01 = request.form["col01"]
    col02 = request.form["col02"]
    col03 = request.form["col03"]
    cnt = MyDao().myinsert(col01, col02, col03)
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)

@app.route('/sample_upd.ajax', methods=['POST'])
def sample_upd_ajax():
    col01 = request.form["col01"]
    col02 = request.form["col02"]
    col03 = request.form["col03"]
    cnt = MyDao().myupdate(col01, col02, col03)
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)

@app.route('/sample_del.ajax', methods=['POST'])
def sample_del_ajax():
    col01 = request.form["col01"]
    cnt = MyDao().mydelete(col01)
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)


if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    