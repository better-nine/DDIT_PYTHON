from flask import Flask,render_template, jsonify, request, session, redirect, escape, send_file
from datetime import timedelta
import cx_Oracle, os
from openpyxl import load_workbook 
from werkzeug.utils import secure_filename
from day42_sul.mydao_suser import MyDao_Suser
from day42_sul.mydao_survey import MyDao_Survey
from day42_sul.mydao_detail import MyDao_Detail
from day42_sul.mydao_starget import MyDao_Starget
from day42_sul.mydao_sresult import MyDao_Sresult
from day42_sul.mymail import Mymail
from day42_sul.mysms import MySms
from day42_sul.mydao_snotice import MyDao_Snotice

#업로드 절대경로 전역변수 선언
DIR_UPLOAD = 'D:/workspace_python/HELLOAI2/day42_sul/static/upload/'

app = Flask(__name__, static_url_path="", static_folder="static")
app.secret_key = b'asdasd'
 
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1)
    

def getSession():
    user_id =""
    try:
        user_id = str(escape(session["user_id"]))
    except : 
        pass
    
    if user_id == "" :
        return False, user_id
    else :
        return True, user_id
   
   
@app.route('/')
@app.route('/main')
def main():
    return render_template('main.html')



@app.route('/sview')
def sview():
    survey_id = request.args.get('survey_id')
    st_mobile = request.args.get('st_mobile')
    list = MyDao_Detail().myselect(survey_id)
    q_cnt = len(list)
    
    return render_template('sview.html', list=list, q_cnt=q_cnt, survey_id=survey_id, st_mobile=st_mobile)

  
@app.route('/sresult_submit.ajax', methods=['POST'])
def sresult_submit_ajax():
    survey_id = request.form["survey_id"]
    st_mobile = request.form["st_mobile"]
    ans = request.form["ans"]
    
    cnt = MyDao_Sresult().myinsert_ans(survey_id, st_mobile, ans)
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)






@app.route('/logout')
def logout():
    session.clear()
    return redirect('main')
    #return render_template('main.html')


@app.route('/join_ajax', methods=['POST'])
def join_ajax():
    user_id = request.form["user_id"]
    pwd = '1'
    user_name = request.form["user_name"]
    birth = request.form["birth"]
    mobile = request.form["mobile"]
    email = request.form["email"]

    cnt = MyDao_Suser().myinsert(user_id, pwd, user_name, birth, mobile, email)
    
    content = user_name+"님, 당신의 계정은 "+user_id+"이고 비밀번호는 1입니다. 로그인 후 변경 바랍니다."
    
    Mymail().mysendmail(email,"설문조사 회원가입을 축하드립니",content)#가입 완료한 사람들 이메일 보내주는 로직 삽입
    
    
    
    
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)
 

@app.route('/dupl_ajax', methods=['POST'])
def dupl_ajax():
    user_id = request.form["user_id"] 

    list = MyDao_Suser().mydupl(user_id)
 
    cnt= len(list) #리스트에 사용자 정보가 들어있기 때문에 1 이상일 경우에는 로그인이 성공적으로 된 것임
    msg = ""
    if cnt == 1 :
        msg = "ng"
    else:
        msg = "ok"
    
    return jsonify(msg = msg)
 

@app.route('/login_ajax', methods=['POST'])
def login_ajax():
    user_id = request.form["user_id"] 
    pwd = request.form["pwd"] 

    list = MyDao_Suser().mylogin(user_id, pwd)
 
    cnt= len(list) #리스트에 사용자 정보가 들어있기 때문에 1 이상일 경우에는 로그인이 성공적으로 된 것임
    
    msg = ""
    if cnt == 1 :
        #session['user_id'] = user_id
        #session['pwd'] = pwd
        session['user_id'] = list[0]['user_id']
        session['user_name'] = list[0]['user_name']
        
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)
 
 
@app.route('/suser')
def suser():
    flag_ses, user_id = getSession()
 
    if not flag_ses :
        return redirect('login.html')
    
    list = MyDao_Suser().myselect()
    return render_template('suser.html',list=list)
    

@app.route('/suser_ins.ajax', methods=['POST'])
def suser_ins_ajax():
    user_id = request.form["user_id"]
    pwd = request.form["pwd"]
    user_name = request.form["user_name"]
    birth = request.form["birth"]
    mobile = request.form["mobile"]
    email = request.form["email"]
    
    in_date = request.form["in_date"]
    in_user_id = str(escape(session["user_id"]))
    up_date = request.form["up_date"]
    up_user_id = str(escape(session["user_id"]))
    
    cnt = MyDao_Suser().myinsert(user_id, pwd, user_name, mobile, birth, email, in_date, in_user_id, up_date, up_user_id)
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
    in_user_id = str(escape(session["user_id"]))
    up_date = request.form["up_date"]
    up_user_id = str(escape(session["user_id"]))
    
    cnt = MyDao_Suser().myupdate(user_id, pwd, user_name, mobile, birth, email, in_date, in_user_id, up_date, up_user_id)
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
    flag_ses, user_id = getSession()
    
    if not flag_ses :
        return redirect('login.html')
    
    in_user_id = str(escape(session["user_id"]))
    list = MyDao_Survey().myselect(in_user_id)
    return render_template('survey.html',list=list)
  
@app.route('/survey_ins.ajax', methods=['POST'])
def survey_ins_ajax():
    survey_id = request.form["survey_id"]
    title = request.form["title"]
    content = request.form["content"]
    interview_cnt = request.form["interview_cnt"]
    deadline = request.form["deadline"]
    
    in_date = request.form["in_date"]
    in_user_id = str(escape(session["user_id"]))
    up_date = request.form["up_date"]
    up_user_id = str(escape(session["user_id"]))
    
    cnt = MyDao_Survey().myinsert(survey_id, title, content, interview_cnt, deadline, in_user_id, up_user_id)
    
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
    in_user_id = str(escape(session["user_id"]))
    up_date = request.form["up_date"]
    up_user_id = str(escape(session["user_id"]))
    
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
    survey_id = request.args.get("survey_id")
     
    flag_ses, user_id = getSession()
    
    if not flag_ses :
        return redirect('login.html')
    
    list = MyDao_Detail().myselect(survey_id)
    return render_template('detail.html', list=list, survey_id=survey_id)
 

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
    in_user_id = str(escape(session["user_id"]))
    up_date = request.form["up_date"]
    up_user_id = str(escape(session["user_id"]))
    cnt = MyDao_Detail().myinsert(survey_id, s_seq, question, a1, a2, a3, a4, in_user_id, up_user_id)
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
    in_user_id = str(escape(session["user_id"]))
    up_date = request.form["up_date"]
    up_user_id = str(escape(session["user_id"]))
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



#############################################################################################
@app.route('/starget')
def starget():
    survey_id = request.args.get("survey_id")
    
    flag_ses, user_id = getSession()
    
    if not flag_ses :
        return redirect('login.html')
    
    list = MyDao_Starget().myselect(survey_id)
    return render_template('starget.html',list=list, survey_id = survey_id)


 
############# 폼 업로드 -----------------------------------------------

@app.route('/starget_form')
def starget_form():
    survey_id = request.args.get("survey_id")
    flag_ses, user_id = getSession()
    if not flag_ses :
        return redirect('login.html')
    return render_template('starget_form.html', survey_id = survey_id)
 
@app.route("/upload", methods = ['POST'])    #url-mapping
def upload():
    survey_id = request.form["survey_id"]
    
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join('D:/workspace_python/HELLOAI2/day41_sul_homework/static/upload/', filename))
    #upload_path = 'D:/workspace_python/HELLOAI2/day41_sul/static/upload/'
    #file.save(upload_path+filename, data_only=True)
    
    print("survey_id ",survey_id," :파일 업로드 완료 ",filename.split('.')[-1])
    
    if filename.split('.')[-1]=='xlsx' :
        temp_list = Excel_list();
        print(temp_list)
        cnt = intoDB(temp_list, survey_id)
    else :
        cnt = 0
    return render_template('upload.html', cnt=cnt)
    
def Excel_list():    
    load_wb = load_workbook("D:/workspace_python/HELLOAI2/day41_sul_homework/static/upload/myexel.xlsx", data_only=True)
    load_ws = load_wb['시트1']
    
    insert_list =[]
    num = 2
    while load_ws['B'+str(num)].value != None :
        name = load_ws['A'+str(num)].value
        number = load_ws['B'+str(num)].value
        insert_list.append({'name':name,'number':number})
        num += 1  
        print(insert_list)  
        
    return insert_list
    
def intoDB(insert_list, survey_id):
    flag_ses, user_id = getSession()
    if not flag_ses :
        return redirect('login.html')
    
    cnt = 0
    st_mobile = ""
    complete_yn = "n"
    in_user_id = user_id
    up_user_id = user_id
    
    for i in insert_list:
        st_mobile = i['number'].replace("-", "")
        cnt += MyDao_Starget().myinsert(survey_id, st_mobile, complete_yn, in_user_id, up_user_id)
    return cnt

########### --------------------------------- -------------------------------------------------------------

@app.route('/starget_sms.ajax', methods=['POST'])
def starget_sms_ajax():
    survey_id = request.form["survey_id"]
    
    list = MyDao_Starget().myselect(survey_id)
    
    print(list)
    for i in list:
        mobile = i['st_mobile']
        url = 'http://192.168.41.27:5000/sview?survey_id='+survey_id+'&st_mobile='+i['st_mobile']
        MySms().mysendSms(mobile, url)
    
    msg = ""
    if len(list) > 0 :
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)
 
 
 

@app.route('/starget_ins_ajax', methods=['POST'])
def starget_ins_ajax():
    survey_id = request.form["survey_id"]
    st_mobile = request.form["st_mobile"]
    complete_yn = request.form["complete_yn"]
    
    in_user_id = str(escape(session["user_id"]))
    up_user_id = str(escape(session["user_id"]))
    cnt = MyDao_Starget().myinsert(survey_id, st_mobile, complete_yn, in_user_id, up_user_id)
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)

@app.route('/starget_upd_ajax', methods=['POST'])
def starget_upd_ajax():
    survey_id = request.form["survey_id"]
    st_mobile = request.form["st_mobile"]
    complete_yn = request.form["complete_yn"]
    
    up_user_id = str(escape(session["user_id"]))
    
    cnt = MyDao_Starget().myupdate(survey_id, st_mobile, complete_yn, up_user_id)
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)

@app.route('/starget_del_ajax', methods=['POST'])
def starget_del_ajax():
    survey_id = request.form["survey_id"]
    st_mobile = request.form["st_mobile"] 
    
    cnt = MyDao_Starget().mydelete(survey_id, st_mobile)
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)



#############################################################################################
@app.route('/sresult')
def sresult():
    flag_ses, user_id = getSession()
    survey_id = request.args.get("survey_id")

    if not flag_ses :
        return redirect('login.html')
    
    list = MyDao_Sresult().myselect_graph(survey_id)
    print(list)
    
    return render_template('sresult.html', list=list, enumerate=enumerate)
 
  
@app.route('/sresult_ins.ajax', methods=['POST'])
def sresult_ins_ajax():
    survey_id = request.form["survey_id"]
    s_seq = request.form["s_seq"]
    st_mobile = request.form["st_mobile"]
    answer = request.form["answer"]
    
    in_date = request.form["in_date"]
    in_user_id = str(escape(session["user_id"]))
    up_date = request.form["up_date"]
    up_user_id = str(escape(session["user_id"]))
    cnt = MyDao_Sresult().myinsert(survey_id, s_seq, st_mobile, answer, in_date, in_user_id, up_date, up_user_id)
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)

@app.route('/sresult_upd.ajax', methods=['POST'])
def sresult_upd_ajax():
    survey_id = request.form["survey_id"]
    s_seq = request.form["s_seq"]
    st_mobile = request.form["st_mobile"]
    answer = request.form["answer"]
    
    in_date = request.form["in_date"]
    in_user_id = str(escape(session["user_id"]))
    up_date = request.form["up_date"]
    up_user_id = str(escape(session["user_id"]))
    cnt = MyDao_Sresult().myupdate(answer, up_user_id, survey_id, s_seq, st_mobile)
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)

@app.route('/sresult_del.ajax', methods=['POST'])
def sresult_del_ajax():
    survey_id = request.form["survey_id"]
    s_seq = request.form["s_seq"]
    st_mobile = request.form["st_mobile"]
    
    cnt = MyDao_Sresult().mydelete(survey_id, s_seq, st_mobile)
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)

#############################################################################################
import datetime 
now = datetime.datetime.now()
formattedDate = now.strftime("%Y%m%d%H%M%S_")

@app.route('/snotice_list')
def snotice_list():
    flag_ses, user_id = getSession()
    if not flag_ses :
        return redirect('login.html')
    
    list = MyDao_Snotice().myselect_list()
    return render_template('snotice_list.html', list=list, enumerate = enumerate)

@app.route('/snotice_detail')
def snotice_detail():
    b_seq = request.args.get("b_seq")
    MyDao_Snotice().myhit(b_seq)
    
    flag_ses, user_id = getSession()
    if not flag_ses :
        return redirect('login.html')
    obj = MyDao_Snotice().myselect(b_seq)
    return render_template('snotice_detail.html',notice=obj, enumerate = enumerate)

@app.route('/snotice_mod')
def snotice_mod():
    b_seq = request.args.get("b_seq")
    flag_ses, user_id = getSession()
    if not flag_ses :
        return redirect('login.html')
    obj = MyDao_Snotice().myselect(b_seq)
    return render_template('snotice_mod.html',notice=obj, enumerate = enumerate)

@app.route('/snotice_modact', methods=['POST'])
def snotice_modact():
    flag_ses, user_id = getSession()
    if not flag_ses :
        return redirect('login.html')
    
    b_seq = request.form["b_seq"]
    title = request.form["title"]
    display_yn = request.form["display_yn"] 
    content = request.form["content"]
    
    print("---request file")
    file = request.files['file']
    filename = secure_filename(file.filename)
    filename_time = formattedDate + filename
    
    file.save(os.path.join(DIR_UPLOAD, filename_time))
    
    attach_path = ""
    attach_file = "" 
    if file :
        print("---file o")
        attach_path = filename_time #난수 붙은 이름 (저장되는이름)
        attach_file = filename      #원래 이름 
        print(file, filename, filename_time)    
    else :
        print("---file x")
        attach_path = request.form["attach_path"]
        attach_file = request.form["attach_file"]

    cnt = MyDao_Snotice().myupdate("y", title, content, attach_path, attach_file, user_id, b_seq)
    print(cnt)
    return render_template('snotice_modact.html', cnt=cnt, b_seq=b_seq)


@app.route('/snotice_delact')
def snotice_delact():
    b_seq = request.args.get("b_seq")
    flag_ses, user_id = getSession()
    if not flag_ses :
        return redirect('login.html')
    cnt = MyDao_Snotice().mydelete(b_seq) 
    return render_template('snotice_delact.html', cnt=cnt)



@app.route('/snotice_add')
def snotice_add():
    flag_ses, user_id = getSession()
    if not flag_ses :
        return redirect('login.html')
    return render_template('snotice_add.html')

@app.route('/snotice_addact', methods=['POST'])
def snotice_addact():
    flag_ses, user_id = getSession()
    if not flag_ses :
        return redirect('login.html')
    
    file = request.files['file']
    filename = secure_filename(file.filename)
    filename_time = formattedDate + filename
    #파일명 뒤에다 난수를 삽입할 경우 확장자명 뒤에 넣을 때는 보안을 지킬 수 있음 (알 수 없는 파일이 되기 때문에! 나중에 지우면 원본파일 나옴)
    #보안이 딱히 필요치 않은 경우에는 앞에다 삽입하면 됨
    
    file.save(os.path.join(DIR_UPLOAD, filename_time))
    
    title = request.form["title"]
    content = request.form["content"]
    display_yn = "" 
    attach_path = ""
    attach_file = "" 
    
    if file :
        attach_path = filename_time #난수 붙은 이름 (저장되는이름)
        attach_file = filename      #원래 이름 
        print("-----")
        print(file, filename, filename_time)
    else :
        print("file is not found")
    
    cnt = MyDao_Snotice().myinsert(display_yn, title, content, attach_path, attach_file, user_id, user_id)
    return render_template('snotice_addact.html', cnt=cnt )


@app.route('/snitoce_del_ajax', methods=['POST'])
def snitoce_del_ajax():
    flag_ses, user_id = getSession()
    if not flag_ses :
        return redirect('login.html')
    
    b_seq = request.form["b_seq"] 
    attach_path = ""
    attach_file = ""
    
    cnt = MyDao_Snotice().myfile_del(attach_path, attach_file, user_id, b_seq)

    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    return jsonify(msg = msg)


@app.route('/download', methods = ['GET'])
def download():
    attach_path = request.args.get("attach_path")
    attach_file = request.args.get("attach_file")
    
    file_name = DIR_UPLOAD + attach_path
    return send_file(file_name,
                     mimetype='image/png', #다운받는 파일의 타입 설정 
                     attachment_filename = attach_file,# 다운받아지는 파일 이름. 
                     as_attachment=True)










if __name__ == '__main__':
    app.run(host='0.0.0.0')
    
    
    
    
    
    
    
    
    
    
    