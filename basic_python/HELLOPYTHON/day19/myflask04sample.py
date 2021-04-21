from flask import Flask,request
from flask.templating import render_template
import cx_Oracle

def getData():
    connection = cx_Oracle.connect('python','python','localhost:1521/xe')
    cursor = connection.cursor()
    
    sql_str = 'select col01, col02, col03 from sample'
    cursor.execute(sql_str)
    
    list = []    
    for name in cursor:        
        list.append( {'col01':name[0],'col02':name[1],'col03':name[2]})
    
    cursor.close()
    connection.close()
    return list


def myinsert(col01, col02, col03):
    connection = cx_Oracle.connect('python','python','localhost:1521/xe')
    cursor = connection.cursor()
    
    sql_str = "insert into sample(col01, col02, col03) values(:1,:2,:3)"
    cursor.execute(sql_str,(col01, col02, col03))
    cnt = cursor.rowcount
        
    connection.commit()
    cursor.close()
    connection.close()

    return cnt


def myupdate(col01, col02, col03):
    connection = cx_Oracle.connect('python','python','localhost:1521/xe')
    cursor = connection.cursor()
    
    sql_str = "update sample set col02=:1, col03=:2 where col01=:3"
    cursor.execute(sql_str,(col02, col03, col01))
    cnt = cursor.rowcount
     
    connection.commit()
    
    cursor.close()
    connection.close()
    return cnt


def mydelete(col01):
    connection = cx_Oracle.connect('python','python','localhost:1521/xe')
    cursor = connection.cursor()
    
    sql_str = "delete sample where col01=:1"
    cursor.execute(sql_str,(col01,))  #여기 들어가는게 튜플만 인식해서 뒤에 쉼표를 찍어서 튜플인거 알려줘야함 
    cnt = cursor.rowcount
    
    connection.commit()
    cursor.close()
    connection.close()
    return cnt


app = Flask(__name__, static_url_path="", static_folder="static")

@app.route("/sample")    #url-mapping
def sample():
    list = getData()
    print(list)
#     col01 = request.args.get('col01')
#     col02 = request.args.get('col02')
#     col03 = request.args.get('col03')
    return render_template('sample.html', list = list)

@app.route("/sample/insert", methods=['POST'])    #url-mapping
def sampleinsert():
    list = getData()
    col01 = request.form['col01']
    col02 = request.form['col02']
    col03 = request.form['col03']
 
    myinsert(col01, col02, col03)
    return render_template('sample.html', list = list)


@app.route("/sample/update", methods=['POST'])    #url-mapping
def sampleupdate():
    list = getData()
    col01 = request.form['col01']
    col02 = request.form['col02']
    col03 = request.form['col03']
 
    myupdate(col01, col02, col03)
    return render_template('sample.html', list = list)


@app.route("/sample/delete", methods=['POST'])    #url-mapping
def sampledelete():
    list = getData()
    col01 = request.form['col01']
 
    mydelete(col01)
    return render_template('sample.html', list = list)


if __name__ == "__main__":
    app.run(debug=True)
    
