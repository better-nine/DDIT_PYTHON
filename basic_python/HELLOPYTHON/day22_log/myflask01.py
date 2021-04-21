from flask import Flask
from day22_log.mylog import MyLog

mylog = MyLog()

app = Flask(__name__)

@app.route("/h1")    #url-mapping
def h1():
    sql = "h111111111111111111" 
    mylog.logger.debug(sql)
    return "H1"


@app.route("/h2")    #url-mapping
def h2():
    sql = "22222222222222222222 "
    mylog.logger.debug(sql)
    return "H2"



if __name__ == "__main__":
    app.run(debug=True)
#   app.run(host='localhost', port=5000)