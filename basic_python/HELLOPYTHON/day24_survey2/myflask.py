from flask import Flask,render_template, jsonify, request, session, redirect
from datetime import timedelta
import cx_Oracle 
from day24_survey2.mydao_suser import MyDao_Suser
from day24_survey2.mydao_survey import MyDao_Survey
from day24_survey2.mydao_detail import MyDao_Detail

app = Flask(__name__, static_url_path="", static_folder="static")

#세션키
app.secret_key = b'asdasd'
 
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1)
    
    
    
@app.route('/')
@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/login_ajax', methods=['POST'])
def login_ajax():
    user_id = request.form["user_id"]
    pwd = request.form["pwd"] 
    session['user_id'] = user_id
    
    list = MyDao_Suser().mylogin(user_id, pwd)
    cnt= len(list) #리스트에 사용자 정보가 들어있기 때문에 1 이상일 경우에는 로그인이 성공적으로 된 것임
    
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)
 
@app.route('/suser')
def suser():
    
    if 'user_id' in session:
        list = MyDao_Suser().myselect()
        return render_template('suser.html',list=list)
    else :
        return redirect('login.html')
    

@app.route('/suser_ins.ajax', methods=['POST'])
def suser_ins_ajax():
    user_id = request.form["user_id"]
    pwd = request.form["pwd"]
    user_name = request.form["user_name"]
    birth = request.form["birth"]
    mobile = request.form["mobile"]
    email = request.form["email"]
    in_date = request.form["in_date"]
    in_user_id = request.form["in_user_id"]
    up_date = request.form["up_date"]
    up_user_id = request.form["up_user_id"]
    cnt = MyDao_Suser().myinsert(user_id, pwd, user_name, birth, mobile, email)
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)

@app.route('/suser_upd.ajax', methods=['POST'])
def suser_upd_ajax():
    user_id = request.form["user_id"]
    pwd = request.form["pwd"]
    user_name = request.form["user_name"]
    birth = request.form["birth"]
    mobile = request.form["mobile"]
    email = request.form["email"]
    in_date = request.form["in_date"]
    in_user_id = request.form["in_user_id"]
    up_date = request.form["up_date"]
    up_user_id = request.form["up_user_id"]
    cnt = MyDao_Suser().myupdate(user_id, pwd, user_name, birth, mobile, email, up_user_id)
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)

@app.route('/suser_del.ajax', methods=['POST'])
def suser_del_ajax():
    user_id = request.form["user_id"]
    cnt = MyDao_Suser().mydelete(user_id)
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)

#############################################################################################
@app.route('/survey')
def survey():
    if 'user_id' in session:
        list = MyDao_Survey().myselect()
        return render_template('survey.html',list=list)
    else :
        return redirect('login.html')

@app.route('/survey_ins.ajax', methods=['POST'])
def survey_ins_ajax():
    survey_id = request.form["survey_id"]
    title = request.form["title"]
    content = request.form["content"]
    interview_cnt = request.form["interview_cnt"]
    deadline = request.form["deadline"]
    
    in_date = request.form["in_date"]
    in_user_id = request.form["in_user_id"]
    up_date = request.form["up_date"]
    up_user_id = request.form["up_user_id"]
    cnt = MyDao_Survey().myinsert(survey_id, title, content, interview_cnt, deadline, in_user_id)
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)

@app.route('/survey_upd.ajax', methods=['POST'])
def survey_upd_ajax():
    survey_id = request.form["survey_id"]
    title = request.form["title"]
    content = request.form["content"]
    interview_cnt = request.form["interview_cnt"]
    deadline = request.form["deadline"]
    
    in_date = request.form["in_date"]
    in_user_id = request.form["in_user_id"]
    up_date = request.form["up_date"]
    up_user_id = request.form["up_user_id"]
    cnt = MyDao_Survey().myupdate(survey_id, title, content, interview_cnt, deadline, up_user_id)
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)

@app.route('/survey_del.ajax', methods=['POST'])
def survey_del_ajax():
    survey_id = request.form["survey_id"]
    cnt = MyDao_Survey().mydelete(survey_id)
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)



#############################################################################################
@app.route('/detail')
def detail():
    if 'user_id' in session:
        list = MyDao_Detail().myselect()
        return render_template('detail.html',list=list)
    else :
        return redirect('login.html')

@app.route('/detail_ins_ajax', methods=['POST'])
def detail_ins_ajax():
    survey_id = request.form["survey_id"]
    s_seq = request.form["s_seq"]
    question = request.form["question"]
    a1 = request.form["a1"]
    a2 = request.form["a2"]
    a3 = request.form["a3"]
    a4 = request.form["a4"]
    
    in_date = request.form["in_date"]
    in_user_id = request.form["in_user_id"]
    up_date = request.form["up_date"]
    up_user_id = request.form["up_user_id"]
    cnt = MyDao_Detail().myinsert(survey_id, s_seq, question, a1, a2, a3, a4, in_user_id, up_date, up_user_id)
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)

@app.route('/detail_upd_ajax', methods=['POST'])
def detail_upd_ajax():
    survey_id = request.form["survey_id"]
    s_seq = request.form["s_seq"]
    question = request.form["question"]
    a1 = request.form["a1"]
    a2 = request.form["a2"]
    a3 = request.form["a3"]
    a4 = request.form["a4"]
    
    in_date = request.form["in_date"]
    in_user_id = request.form["in_user_id"]
    up_date = request.form["up_date"]
    up_user_id = request.form["up_user_id"]
    cnt = MyDao_Detail().myupdate(survey_id, s_seq, question, a1, a2, a3, a4, up_user_id)
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)

@app.route('/detail_del_ajax', methods=['POST'])
def detail_del_ajax():
    survey_id = request.form["survey_id"]
    s_seq = request.form["s_seq"]
    
    cnt = MyDao_Detail().mydelete(survey_id, s_seq)
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)






















if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    