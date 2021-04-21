from flask import Flask,request

app = Flask(__name__)

@app.route("/gugu")    #url-mapping


def gugu():
    dan = request.args.get('dan')

    gob = dan+"*1="+ str(int(dan)*1) +"<br>"
    gob += dan+ "*2="+ str(int(dan)*2) +"<br>"
    gob += dan+ "*3="+ str(int(dan)*3) +"<br>"
    gob += dan+ "*4="+ str(int(dan)*4) +"<br>"
    gob += dan+ "*5="+ str(int(dan)*5) +"<br>"
    gob += dan+ "*6="+ str(int(dan)*6) +"<br>"
    gob += dan+ "*7="+ str(int(dan)*7) +"<br>"
    gob += dan+ "*8="+ str(int(dan)*8) +"<br>"
    gob += dan+ "*9="+ str(int(dan)*9) +"<br>"
    return gob

def hello():
    return "Hello Flasksksasdasdasdksksksksk!"

if __name__ == "__main__":
    app.run(debug=True)
#   app.run(host='localhost', port=5000)


