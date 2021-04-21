from flask import Flask,render_template, jsonify, request



import cx_Oracle

def getData():
    conn = cx_Oracle.connect('python/python@localhost:1521/xe')
    cs = conn.cursor()
    rs = cs.execute('select col01,col02,col03 FROM sample')

    list = []

    for record in rs:
        list.append({'col01':record[0],'col02':record[1],'col03':record[2]})

    cs.close()
    conn.close()
    
    return list
    
def myinsert(col01,col02,col03):
    conn = cx_Oracle.connect('python/python@localhost:1521/xe')
    cs = conn.cursor()
    sql = "insert into sample (col01,col02,col03) values (:1,:2,:3)"
    cs.execute(sql,(col01,col02,col03))
    cnt = cs.rowcount
    
    cs.close()
    conn.commit()
    conn.close()    
    return cnt
    
    
def myupdate(col01,col02,col03):
    conn = cx_Oracle.connect('python/python@localhost:1521/xe')
    cs = conn.cursor()
    sql = "update sample set col02=:1,col03=:2 where col01=:3"
    cs.execute(sql,(col02,col03,col01))
    cnt = cs.rowcount
    
    cs.close()
    conn.commit()
    conn.close()    
    return cnt    

def mydelete(col01):
    conn = cx_Oracle.connect('python/python@localhost:1521/xe')
    cs = conn.cursor()
    sql = "delete from sample where col01 = :1"
    cs.execute(sql,(col01,))
    cnt = cs.rowcount
    
    cs.close()
    conn.commit()
    conn.close()    
    return cnt  

app = Flask(__name__, static_url_path="", static_folder="static")

@app.route('/sample')
def render():
    list = getData()
    return render_template('sample.html',list=list)

@app.route('/sample_ins.ajax', methods=['POST'])
def sample_ins_ajax():
    col01 = request.form["col01"]
    col02 = request.form["col02"]
    col03 = request.form["col03"]
    cnt = myinsert(col01, col02, col03)
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
    cnt = myupdate(col01, col02, col03)
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)

@app.route('/sample_del.ajax', methods=['POST'])
def sample_del_ajax():
    col01 = request.form["col01"]
    cnt = mydelete(col01)
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)


if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    