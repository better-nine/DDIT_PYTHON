from flask import Flask, request, jsonify, render_template, session, escape, redirect, send_file
from werkzeug.utils import secure_filename
from sendmail import SendMail
from datetime import timedelta, datetime
import os, random, string

from dao_member import DaoMember
from dao_scrap import DaoScrap
from dao_answer import DaoAnswer
from dao_after import DaoAfter
from mydao_board import MyDaoBoard
from mydao_memo import MyDaoMemo
from mydao_notice import MyDaonotice
from dao_admin import DaoAdmin
from dao_cmt import DaoCmt
from scraping import Scrap
from save_excel import Excel
from dao_interview import DaoInterview
from dao_calender import DaoCalender
from dao_visit import DaoVisit
from dao_graph import DaoGraph
  
DIR_UPLOAD = "X:/" 
app = Flask(__name__, static_url_path='', static_folder='static')
app.secret_key = b'asdasd'

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1000)

@app.route('/')
@app.route('/main_view')
def main():
    mem_id = request.args.get("mem_id")
    select_mydday_title = DaoMember().select_mydday_title(mem_id)
    select_mydday_date = DaoMember().select_mydday_date(mem_id)
    a = str(select_mydday_title)
    b = a[2:-2]
    
    c = str(select_mydday_date)
    d = c[1:-1]
    
    mem_cnt = DaoMember().counter()
    visit_cnt = DaoVisit().counter()
    news_1 = Scrap().news_list('IT일반')
    news_2 = Scrap().news_list('컴퓨터')
    news_3 = Scrap().news_list('모바일')
    news_4 = Scrap().news_list('인터넷')
    news_5 = Scrap().news_list('보안')
    
    return render_template('main_view.html', select_mydday_title=b, select_mydday_date=d, mem_cnt=mem_cnt, visit_cnt = visit_cnt, news_1 = news_1, news_2 = news_2, news_3 = news_3, news_4 = news_4, news_5 = news_5, enumerate = enumerate)

def getSession():
    mem_id =""
    try:
        mem_id = str(escape(session["mem_id"]))
    except : 
        pass
    
    if mem_id == "" :
        return False, mem_id 
    else :
        return True, mem_id 
   
@app.route('/logout')
def logout():
    session.clear()
    mem_id = ''
    select_mydday_title = ''
    select_mydday_date = ''
    
    mem_cnt = DaoMember().counter()
    visit_cnt = DaoVisit().counter()
    news_1 = Scrap().news_list('IT일반')
    news_2 = Scrap().news_list('컴퓨터')
    news_3 = Scrap().news_list('모바일')
    news_4 = Scrap().news_list('인터넷')
    news_5 = Scrap().news_list('보안')
    
    return render_template('main_view.html', select_mydday_title=select_mydday_title, select_mydday_date=select_mydday_date, visit_cnt=visit_cnt, mem_cnt=mem_cnt, news_1 = news_1, news_2 = news_2, news_3 = news_3, news_4 = news_4, news_5 = news_5, enumerate = enumerate)

@app.route('/login')
def login_view():
    return render_template('login.html')

@app.route('/login.ajax', methods=['POST'])
def login():
    mem_id = request.form["mem_id"] 
    mem_pass = request.form["mem_pass"]
    
    if mem_id=='admin' :
        list = DaoAdmin().login(mem_id, mem_pass)
        cnt = len(list)
        if cnt == 1 :
            session['mem_id'] = list[0]['admin_id']
            DaoVisit().merge(mem_id) 
            msg = "admin"
        else:
            msg = "ng"
        return jsonify(msg = msg)

    else :
        list = DaoMember().login(mem_id, mem_pass)
        cnt = len(list)    
        try :    
            if list[0]['del_yn'] == 'Y':
                return jsonify(msg = 'out')
            elif list[0]['del_yn'] == 'D': 
                return jsonify(msg = 'blind')
        except :
                return jsonify(msg = 'login_err')
    
    if cnt == 1 :
        session['mem_id'] = list[0]['mem_id']
        session['mem_name'] = list[0]['mem_name']
        DaoVisit().merge(mem_id) 
        
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)

#################################################################

@app.route('/join')
def join_view():
    return render_template('join.html')

@app.route('/join.ajax', methods=['POST'])
def join():
    mem_id = request.form["mem_id"]
    mem_name = request.form["mem_name"]
    mem_pass = request.form["mem_pass"]
    mem_mail = request.form["mem_mail"]
    mem_job = request.form["mem_job"]
    dday_title = request.form["dday_title"]
    dday_date = request.form["dday_date"]
    
    cnt = DaoMember().insert(mem_id, mem_name, mem_pass, mem_mail, mem_job, dday_title, dday_date)
    
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)    

@app.route('/kakao_join.ajax', methods=['POST'])
def kakao_join():
    mem_id = 'kakao_' + request.form["mem_id"]
    mem_name = request.form["mem_name"]
    mem_mail = request.form["mem_mail"]
    mem_job = '백수'
    dday_title = 'D-DAY'
    
    cnt = DaoMember().kakao_join(mem_id, mem_name, mem_mail, mem_job, dday_title)

    if cnt == 1 :
        session['mem_id'] = mem_id
        session['mem_name'] = mem_name
        
        msg = "ok"
    else:
        msg = "ng"
    return jsonify(msg = msg)

@app.route('/dupl_id.ajax', methods=['POST'])
def dupl_id():
    mem_id = request.form["mem_id"] 
    list = DaoMember().dupl_id(mem_id)
    cnt= len(list) 
    msg = ""
    if cnt == 1 :
        msg = "ng"
    else:
        msg = "ok"
    return jsonify(msg = msg)

@app.route('/dupl_email.ajax', methods=['POST'])
def dupl_email():
    mem_mail = request.form["mem_mail"] 
    list = DaoMember().dupl_email(mem_mail)
    cnt= len(list)  
    msg = ""
    if cnt == 1 :
        msg = "ng"
    else:
        msg = "ok"
    return jsonify(msg = msg)  
   
@app.route('/find_info')
def find_info_view():
    return render_template('find_info.html')

@app.route('/find_id.ajax')
def find_id():
    mem_mail = request.args.get("mem_mail")
    list = DaoMember().dupl_email(mem_mail)
    
    try :
        mem_id = list[0]['mem_id']
        cnt= len(list) 
        msg = ""
        if cnt == 1 :
            msg = "ok"
        else:
            msg = "ng"
    except :
        mem_id = " 존재하지 않습니다"
        msg = "ng"
        
    return jsonify(msg = msg, mem_id = mem_id) 

@app.route('/find_pass.ajax')
def find_pass():
    mem_id = request.args.get("mem_id")
    dupllist = DaoMember().dupl_id(mem_id)
    cnt= len(dupllist) 
    
    msg = ""
    if cnt == 1 :
        temp_alpha = list(string.ascii_letters)
        temp_num = random.randrange(0,999999)
        temp_pass = ''.join(random.sample(temp_alpha,2))+str(temp_num)
        
        set_tempPwd = DaoMember().set_temp_pass(temp_pass, mem_id)
        content = mem_id+"님의 임시 비밀번호는 "+temp_pass+"입니다. 로그인 후 변경하시기 바랍니다."
        SendMail().sendmail(dupllist[0]['mem_mail'], "[백수탈출] 비밀번호 안내", content)
        msg = "ok"
    else:
        msg = "ng"
        
    return jsonify(msg = msg) 

##########################################관리자 로그인 yj.test
@app.route('/login_admin')
def login_admin_view():
    return render_template('set_view.html')

@app.route('/login_admin.ajax', methods=['POST'])
def login_admin():
    admin_id = request.form["admin_id"] 
    admin_pass = request.form["admin_pass"] 
    list =DaoAdmin().login(admin_id, admin_pass)

    msg = ""
    if len(list) == 1 :
        session['admin_id'] = list[0]['admin_id']
        
        msg = "ok"
    else:
        msg = "ng"
    return jsonify(msg = msg)

@app.route('/logout_admin')
def logout_admin():
    session.clear()
    return render_template('set_view.html')

#########################################################   
@app.route('/mypage')  
def mypage():
    flag_ses, mem_id = getSession()
    if not flag_ses :
        return redirect('login')
    
    list = DaoMember().select_mypage(mem_id) 
        
    return render_template('mypage.html', list = list[0])
        
@app.route('/mymod') 
def mymod():
    flag_ses, mem_id = getSession()
    if not flag_ses :
        return redirect('login')
    
    list = DaoMember().select_mypage(mem_id) 
    
    return render_template('mymod.html', list = list[0])

@app.route('/mymod.ajax', methods=['POST'])  
def mymod_act():
    flag_ses, mem_id = getSession()
    if not flag_ses :
        return redirect('login')
    
    mem_id = request.form["mem_id"]
    mem_name = request.form["mem_name"]
    mem_pass = request.form["mem_pass"]
    mem_mail = request.form["mem_mail"]
    mem_job = request.form["mem_job"]
    
    if mem_job =='' :
        mem_job = '백수'
    
    dday_title = request.form["dday_title"]
    dday_date = request.form["dday_date"]
    
    dupl_mail = DaoMember().dupl_email(mem_mail)
    
    if len(dupl_mail)!=0 :
        if mem_id != dupl_mail[0]['mem_id'] :
            return jsonify(msg = "mail_exist")  
    
    cnt = DaoMember().update(mem_id, mem_name, mem_pass, mem_mail, mem_job, dday_title, dday_date)
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
         
    return jsonify(msg = msg) 

@app.route('/quit.ajax') 
def quit():       
    flag_ses, mem_id = getSession()
    if not flag_ses :
        return redirect('login')
    
    mem_id = request.args.get("mem_id")
    cnt = DaoMember().delete(mem_id) 
    msg = ""
    if cnt == 1 :
        session.clear()
        msg = "ok"
    else:
        msg = "ng"
         
    return jsonify(msg = msg) 

#########################################################   
@app.route('/job_list') #채용정보
def job_list():
    flag_ses, mem_id = getSession()
    if not flag_ses :
        return redirect('login')
    
    try :
        myinfo = DaoMember().select_mypage(mem_id)
        job_list_all = Scrap().job_list(myinfo[0]['mem_job'])
    except :
        jobs = Scrap().job_list('웹개발자')
        return render_template('job_list_admin.html', jobs = jobs, enumerate = enumerate)
    
    return render_template('job_list.html', list_all = job_list_all, enumerate = enumerate)

@app.route('/job_search') #채용정보
def job_search():
    job_name = request.args.get("job_name")
    
    if job_name == '웹&앱개발자' :
        job_name == '웹개발자'
    
    jobs = Scrap().job_list(job_name)
    
    return render_template('job_list_admin.html', jobs = jobs, enumerate = enumerate)

@app.route('/job_add.ajax')
def job_add():
    flag_ses, mem_id = getSession()
    if not flag_ses :
        return redirect('login')
    
    scrap_name = request.args.get("scrap_name")
    scrap_url = request.args.get("scrap_url")
    rec_idx = request.args.get("rec_idx")
    scrap_comp = request.args.get("scrap_comp")
    
    dupl_list = DaoScrap().dupl_mine(scrap_name, mem_id)
    if len(dupl_list) != 0 :
        msg = "exist"
        return jsonify(msg = msg)  
    else :
        cnt = DaoScrap().insert(scrap_name, scrap_comp, scrap_url+"&rec_idx="+rec_idx, mem_id)
        msg = ""
        if cnt == 1 :
            msg = "ok"
        else:
            msg = "ng"
        return jsonify(msg = msg)  

@app.route('/job_del.ajax')
def job_del():
    flag_ses, mem_id = getSession()
    if not flag_ses :
        return redirect('login')
    
    scrap_seq = request.args.get("scrap_seq")
    cnt = DaoScrap().delete(scrap_seq, mem_id)
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
    return jsonify(msg = msg) 
           
@app.route('/job_list_selected') #채용정보
def job_list_selected():
    flag_ses, mem_id = getSession()
    if not flag_ses :
        return redirect('login')
    
    list_selected = DaoScrap().select_mine(mem_id)
    
    content = "현재 스크랩한 채용정보가 존재하지 않습니다."
    
    return render_template('job_list_selected.html',list_selected = list_selected, enumerate = enumerate, content = content)
#######################################################

@app.route('/after_list') #면접 후기 리스트
def after_list():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login")    
    search = request.args.get('search', '')
    
    if search:
        list = DaoAfter().select_search(search)
        return render_template('after_list.html', list=list,enumerate=enumerate, search=search)
    
    list = DaoAfter().select_list()
    return render_template('after_list.html' ,list=list,enumerate=enumerate)

@app.route("/after_detail")
def after_detail():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login")    
    
    after_seq = request.args.get('after_seq')
    obj = DaoAfter().select(after_seq)
    return render_template('after_detail.html', after=obj, enumerate=enumerate)
    
@app.route('/after_mod.ajax') #면접 후기 상세 수정
def after_mod_ajax():
    
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login")  
      
    after_seq = request.form["after_seq"]
    after_title = request.form["after_title"]
    after_content = request.form["after_content"]
    after_content = after_content.replace('\n','<br/>')
    
    attach_file = request.form["attach_file"]
    attach_path = request.form["attach_path"]

    in_date = request.form["in_date"]
    up_date = request.form["up_date"]

    cnt = DaoAfter().update(after_seq, after_title, after_content, attach_file, attach_path, in_date, user_id, up_date, user_id)
    
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"

    return jsonify(msg = msg)

@app.route("/after_mod")
def after_mod():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login")    

    after_seq = request.args.get('after_seq')
    obj = DaoAfter().select(after_seq)
    return render_template('after_mod.html', after=obj,enumerate=enumerate)

@app.route("/after_modact", methods=['POST'])
def after_modact():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login")

    after_seq = request.form["after_seq"]
    after_title = request.form["after_title"]
    after_content = request.form["after_content"]
    after_content = after_content.replace('\n','<br/>')
    attach_file_old = request.form["attach_file"]
    attach_path_old = request.form["attach_path"]
    
    if attach_file_old == 'None' :
        attach_file_old = ""
        attach_path_old = ""
    
    file = request.files['file']        
    attach_file_temp = secure_filename(file.filename)
    
    if '.' not in list(attach_file_temp):
        attach_file_temp = str(datetime.today().strftime("%Y%m%d%H%M%S"))+'_untitled.'+attach_file_temp
        
    attach_path_temp = str(datetime.today().strftime("%Y%m%d%H%M%S")) +"_"+ attach_file_temp  
    file.save(os.path.join(DIR_UPLOAD, attach_path_temp))
    
    attach_path = ""
    attach_file = ""
    if file :
        attach_path = attach_path_temp 
        attach_file = attach_file_temp
                
        num1 = attach_path.count('.')
        num2 = attach_file.count('.')
        
        for i in range(num1-1):
            attach_path = attach_path.replace('.','',1)
        for i in range(num2-1):
            attach_file = attach_file.replace('.','',1)
        
        print("file o",attach_file, attach_path)
    else:
        attach_path = attach_path_old 
        attach_file = attach_file_old
        print("file X")
    
    cnt = DaoAfter().update(after_seq, after_title, after_content, attach_file, attach_path ,user_id)
    
    return render_template('after_modact.html', cnt=cnt, after_seq=after_seq, enumerate=enumerate)

@app.route("/after_add")
def after_add():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login")    
    return render_template('after_add.html',enumerate=enumerate)

@app.route("/after_addact", methods=['POST'])
def after_addact():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login")   
    
    after_title         = request.form["after_title"]
    after_content       = request.form["after_content"]
    after_content       = after_content.replace('\n','<br/>')
    file = request.files['file']    
    attach_file_temp = secure_filename(file.filename)
    
    if '.' not in list(attach_file_temp):
        attach_file_temp = str(datetime.today().strftime("%Y%m%d%H%M%S"))+'_untitled.'+attach_file_temp
    
    attach_path_temp = str(datetime.today().strftime("%Y%m%d%H%M%S")) +"_"+ attach_file_temp  
    file.save(os.path.join(DIR_UPLOAD, attach_path_temp))
    
    attach_path = ""
    attach_file = ""
    if file :
        attach_path = attach_path_temp 
        attach_file = attach_file_temp
                
        num1 = attach_path.count('.')
        num2 = attach_file.count('.')
        
        for i in range(num1-1):
            attach_path = attach_path.replace('.','',1)
        for i in range(num2-1):
            attach_file = attach_file.replace('.','',1)
        
        print("file o",attach_file, attach_path)
    else:
        print("file X")

    cnt = DaoAfter().insert('', after_title, after_content, attach_file, attach_path, '', user_id, '', user_id)

    return render_template('after_addact.html', cnt=cnt,enumerate=enumerate)

@app.route('/after_del.ajax', methods=['POST']) 
def after_del_ajax():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login")    
    
    after_seq = request.form["after_seq"]
    cnt = DaoAfter().delete(after_seq)
    
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"

    return jsonify(msg = msg)

@app.route('/after_del_file.ajax', methods=['POST']) 
def after_del_file_ajax():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login")    
    
    after_seq = request.form["after_seq"]
    cnt = DaoAfter().del_img(after_seq)
    
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"

    return jsonify(msg = msg)

@app.route('/download')
def after_download():
    attach_path = request.args.get('attach_path')
    attach_file = request.args.get('attach_file')
    
    file_name = DIR_UPLOAD+"/"+attach_path
    return send_file(file_name,
                     mimetype='image/png',
                     attachment_filename=attach_file,
                     as_attachment=True)

######################################################### 
@app.route('/answer_list') #나의 답변
def answer_list():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login")   
     
    search= request.args.get('search','')
    list = DaoAnswer().select_search(user_id, search)
    return render_template('answer_list.html' , list=list, enumerate=enumerate, user_id =user_id, search=search) 

@app.route('/answer_detail') #답변 디테일
def answer_detail():
    answer_seq = request.args.get('answer_seq')
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login")    
    
    obj = DaoAnswer().select(answer_seq, user_id)
    return render_template('answer_detail.html', answer=obj, enumerate=enumerate)
    
@app.route("/answer_mod")
def answer_mod():
    answer_seq = request.args.get('answer_seq')
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login")    

    obj = DaoAnswer().select(answer_seq, user_id)
    return render_template('answer_mod.html', answer=obj,enumerate=enumerate)

@app.route("/answer_modact", methods=['POST'])
def answer_modact():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login")

    answer_seq = request.form["answer_seq"]
    answer_content = request.form["answer_content"]
    answer_content = answer_content.replace('\n','<br/>')
    
    cnt = DaoAnswer().update(answer_seq, answer_content)
    return render_template('answer_modact.html', cnt=cnt, answer_seq=answer_seq, enumerate=enumerate)

@app.route('/answer_del.ajax' , methods=['POST']) 
def answer_del_ajax():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login")    
    answer_seq = request.form["answer_seq"]

    cnt = DaoAnswer().delete(answer_seq)
    
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"

    return jsonify(msg = msg, cnt=cnt)
        
@app.route('/answer_download')
def answer_download():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login")    
    
    list = DaoAnswer().select_list(user_id)

    Excel().import_excel(user_id, list)
    
    file_name = DIR_UPLOAD+'/My_answer_'+user_id+'.xlsx'
    
    return send_file(file_name,
                     mimetype='image/png',
                     attachment_filename='My_answer_'+user_id+'.xlsx',
                     as_attachment=True)

####################################################### 관리자 화면
@app.route('/user_set') #유저관리
def user_set():
    flag_ses, mem_id = getSession()
    if mem_id!='admin' :
        return redirect('login')
    
    list = DaoMember().select()
    return render_template('user_set.html',list=list, enumerate=enumerate)

@app.route('/user_modact', methods=['POST']) #유저수정 yj.test
def user_modact():
    flag_ses, mem_id = getSession()
    if mem_id!='admin' :
        return redirect('login')
    
    mem_id = request.form['mem_id']
    mem_name = request.form['mem_name']
    mem_mail = request.form['mem_mail']
    mem_job = request.form['mem_job']
    
    cnt =DaoMember().update_mod(mem_id, mem_name, mem_mail, mem_job)
    return render_template('user_modact.html',cnt=cnt,mem_id = mem_id ,enumerate =enumerate)

@app.route('/user_yn.ajax',methods=['POST']) #유저비활성화 yj.test
def user_yn_ajax():
    flag_ses, mem_id = getSession()
    if mem_id!='admin' :
        return redirect('login')
    
    mem_id = request.form["mem_id"]
    cnt =DaoMember().user_yn(mem_id)
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
         
    return jsonify(msg = msg ) 
    
@app.route('/user_act.ajax',methods=['POST']) #유저활성화 yj.test
def user_act_ajax():
    flag_ses, mem_id = getSession()
    if mem_id!='admin' :
        return redirect('login')
    
    mem_id = request.form["mem_id"]
    cnt =DaoMember().user_act(mem_id)
    msg = ""
    if cnt == 1 :
        msg = "ok"
    else:
        msg = "ng"
         
    return jsonify(msg = msg ) 
#########################################################   
@app.route('/notice_list') # 회원페이지 공지사항 목록
def notice_list():
    list = MyDaonotice().myselect_list();
    return render_template('notice_list.html',list=list, enumerate=enumerate)


@app.route('/notice_detail') #회원페이지 공지사항 상세내용
def notice_detail():
    notice_seq = request.args.get("notice_seq");
#      request.form["notice_seq"] 
    
    obj = MyDaonotice().myselect(notice_seq);
    return render_template('notice_detail.html', notice=obj, enumerate=enumerate)

#########################################################   
@app.route('/bot_chat') #면접연습
def bot_chat():
    questions = DaoInterview().select_content() 
    return render_template('bot_chat.html', questions = questions)
        
@app.route('/bot_answer.ajax') #면접연습
def bot_answer():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login")    

    bot_question_seq = request.args.get('bot_question_seq')
    my_answer = request.args.get('my_answer')
    
    if my_answer=='' :
        my_answer = '답변하지 않았습니다.'
    
    cnt = DaoAnswer().insert(user_id, my_answer, bot_question_seq) 
    msg=''
    if cnt == 1 :
        msg ='ok'
    else :
        msg ='ng'
    
    return jsonify(msg = msg)
#########################################################   
@app.route('/calender') #일정캘린더
def calender():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login")    
    list = DaoCalender().select_myplan(user_id)
    date = datetime.today().strftime("%Y%m%d")
    return render_template('calender.html', list = list)

@app.route('/cal_add') #일정 등록
def cal_add():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login")  
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')

    plan_date = str(year)+str(month)+str(day)
    
    return render_template('cal_add.html', plan_date = plan_date)

@app.route('/cal_addact.ajax', methods=['POST']) #일정 등록
def cal_addact():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login")    
    
    plan_date = request.form["plan_date"] 
    plan_title = request.form["plan_title"] 
    plan_content = request.form["plan_content"] 
    plan_content = plan_content.replace('\n','<br/>')

    cnt = DaoCalender().insert(plan_title, plan_content, plan_date, user_id)
    if cnt == 1 :
        msg ='ok'
    else :
        msg ='ng'
    return jsonify(msg = msg)

@app.route('/cal_modact.ajax', methods=['POST']) #일정 등록
def cal_modact():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login")    
    
    plan_seq = request.form["plan_seq"] 
    plan_title = request.form["plan_title"] 
    plan_content = request.form["plan_content"] 
    plan_content = plan_content.replace('\n','<br/>')
    
    cnt = DaoCalender().update(user_id, plan_seq, plan_title, plan_content)
    if cnt == 1 :
        msg ='ok'
    else :
        msg ='ng'
    return jsonify(msg=msg)

@app.route('/cal_mod') #일정 수정
def cal_mod():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login")    
    plan_seq = request.args.get('plan_seq')
    list = DaoCalender().select_detail(plan_seq)
    plan_detail = list[0]
    return render_template('cal_mod.html', plan_detail = plan_detail)
        
@app.route('/cal_delact.ajax') #일정삭제
def cal_delact():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login")    
    plan_seq = request.args.get('plan_seq')
    
    cnt = DaoCalender().delete(plan_seq)
    if cnt == 1 :
        msg ='ok'
    else :
        msg ='ng'
    return jsonify (msg=msg)
        
##################################################### 관리자 화면(이미라)
@app.route('/notice_list_admin') # 관리자페이지 공지사항 목록
def notice_list_admin():
    flag_ses, user_id = getSession()
    if user_id!='admin':
        return redirect("login")    
    
    list = MyDaonotice().myselect_list();
    return render_template('notice_list_admin.html',list=list, enumerate=enumerate)

@app.route('/notice_detail_admin') #관리자페이지 공지사항 상세내용
def notice_detail_admin():
    notice_seq = request.args.get("notice_seq");
#      request.form["notice_seq"] 
    
    obj = MyDaonotice().myselect(notice_seq);
    return render_template('notice_detail_admin.html', notice=obj, enumerate=enumerate)

@app.route('/notice_mod') #관리자페이지 공지사항 수정화면
def notice_mod():
    notice_seq = request.args.get("notice_seq");
    obj = MyDaonotice().myselect(notice_seq)
    return render_template('notice_mod.html',notice=obj, enumerate=enumerate)

@app.route("/notice_modact", methods=['POST'])
def notice_modact_render(): #관리자페이지 공지사항 수정화면 act
    
    notice_seq           = request.form['notice_seq']
    notice_title      = request.form['notice_title']
    notice_content           = request.form['notice_content']
    
    cnt = MyDaonotice().myupdate(notice_seq, notice_title, notice_content, "", '', '', '')
    
    return render_template('notice_modact.html', cnt=cnt, notice_seq=notice_seq, enumerate=enumerate)

@app.route('/notice_add') # 관리자페이지 공지사항 글쓰기
def notice_add():
    return render_template('notice_add.html',  enumerate=enumerate)

@app.route("/notice_addact", methods=['POST'])
def notice_addact_render():
    notice_title  = request.form["notice_title"]
    notice_content       = request.form["notice_content"]
 
    cnt = MyDaonotice().myinsert(notice_title, notice_content, '', '', '', '')
    return render_template('notice_addact.html', cnt=cnt,enumerate=enumerate)

@app.route("/notice_delact")
def notice_delact_render():
    notice_seq = request.args.get('notice_seq')
   
    cnt = MyDaonotice().mydelete(notice_seq)

    return render_template('notice_delact.html', cnt=cnt,enumerate=enumerate)
        
#########################################################   

@app.route('/memo_list') # 메모 목록
def memo_list():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login")    
    
    list = MyDaoMemo().myselect_list(user_id)
    return render_template('memo_list.html',list=list, enumerate=enumerate)

@app.route('/memo_addact') #메모
def memo_add_act():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login")    
    
    memo_content = request.args.get('memo_content')
    cnt = MyDaoMemo().myinsert(memo_content, user_id, user_id)
    
    return render_template('memo_addact.html', cnt=cnt, enumerate=enumerate)

@app.route('/memoSelect.ajax', methods=['POST']) # y,n 결과값 받아오기
def memoSelect_ajax():
    memo_seq = request.form["memo_seq"]
    
    cnt = MyDaoMemo().myselect(memo_seq)
    return jsonify(flag=cnt)

@app.route('/memo_modact') # y,n 수정
def memo_modact():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login")    
    
    memo_yn = request.args.get('memo_yn')
    memo_seq = request.args.get('memo_seq')
    
    cnt = MyDaoMemo().myupdate(memo_yn, memo_seq)
    return render_template('memo_modact.html', cnt=cnt, enumerate=enumerate)

@app.route("/memo_delact")
def memo_delact_render():
    memo_seq = request.args.get('memo_seq')
    cnt = MyDaoMemo().mydelete(memo_seq)

    return render_template('memo_delact.html', cnt=cnt, enumerate=enumerate)

########################################################yj.test권한 주고 추가한 곳
@app.route('/question_list') #질문/건의 리스트
def question_list():
    flag_ses, user_id = getSession()
    search= request.args.get('search','')
    list = MyDaoBoard().select_all_list(search)
    return render_template('question_list.html', mem_id = user_id,list=list, enumerate=enumerate, search=search)
    
@app.route('/question_list_admin') #질문/건의 리스트
def question_list_admin():
    flag_ses, user_id = getSession()
    search= request.args.get('search','')
    list = MyDaoBoard().select_all_list(search)
    return render_template('question_list_admin.html', mem_id = user_id, list=list, enumerate=enumerate, search=search)
    
@app.route('/question_add') #질문/건의 추가 yj
def question_add():
    return render_template('question_add.html',enumerate=enumerate)
  
@app.route('/question_addact' , methods=['POST']) #질문/건의 추가 yj
def question_addact():
    board_title     = request.form['board_title']
    mem_id          = request.form['mem_id']
    board_pass          = request.form['board_pass']
    board_content   = request.form['board_content']
    file            = request.files['file']
    print("file : ", file)
       
    attach_file_temp = secure_filename(file.filename)

    if '.' not in list(attach_file_temp):
        attach_file_temp = str(datetime.today().strftime("%Y%m%d%H%M%S"))+'_untitled.'+attach_file_temp
    
    attach_path_temp = str(datetime.today().strftime("%Y%m%d%H%M%S")) +"_"+ attach_file_temp 
            
    print("first : ", attach_file_temp, attach_path_temp)
    
    file.save(os.path.join(DIR_UPLOAD,attach_path_temp))
    attach_path = ""
    attach_file = ""
    if file :
        attach_path = attach_path_temp 
        attach_file = attach_file_temp
        print("if문 : ", attach_path, attach_file)
                
        num1 = attach_path.count('.')
        num2 = attach_file.count('.')
        
        for i in range(num1-1):
            print("attach_path 포문 -------------------------------")
            attach_path = attach_path.replace('.','',1)
            print(attach_path)
        for i in range(num2-1):
            print("attach_file 포문 -------------------------------")
            attach_file = attach_file.replace('.','',1)
            print(attach_file)
        
        print("file o",attach_file, attach_path)
    else:
        
        print("file X")
    
    cnt = MyDaoBoard().myinsert(board_title, board_content, attach_file, attach_path, '', mem_id, '', mem_id,board_pass)
                 
    return render_template('question_addact.html',enumerate=enumerate,cnt=cnt)

@app.route('/question_mod') #질문/건의 수정
def question_mod():
    board_seq = request.args.get('board_seq')
    obj = MyDaoBoard().myselect(board_seq)
    return render_template('question_mod.html',notice=obj,enumerate=enumerate)

@app.route('/question_modact', methods=['POST']) #질문/건의 수정
def question_modact():
    flag_ses, user_id = getSession()
    board_seq = request.form['board_seq']
    board_title = request.form['board_title']
    board_content = request.form['board_content']
    board_content = board_content.replace('\n','<br/>')
    attach_file_old = request.form['attach_file']
    attach_path_old = request.form['attach_path']
    
    if attach_file_old =="None" :
        attach_file_old =""
        attach_path_old =""
        
    file = request.files['file']
    attach_file_temp =secure_filename(file.filename)
    
    if '.' not in list(attach_file_temp):
        attach_file_temp = str(datetime.today().strftime("%Y%m%d%H%M%S"))+'_untitled.'+attach_file_temp
    
    attach_path_temp = str(datetime.today().strftime("%Y%m%d%H%M%S")) +"_"+ attach_file_temp 
    file.save(os.path.join(DIR_UPLOAD,attach_path_temp))
  
    attach_path = ""
    attach_file = ""
    if file :
        attach_path = attach_path_temp 
        attach_file = attach_file_temp
        
        print("------------------------------")
        print(attach_path, attach_file)
                
        num1 = attach_path.count('.')
        num2 = attach_file.count('.')
        
        for i in range(num1-1):
            print("------------------------------")
            attach_path = attach_path.replace('.','',1)
            print(attach_path)
        for i in range(num2-1):
            print("------------------------------")
            attach_file = attach_file.replace('.','',1)
            print(attach_file)
        
        print("file o",attach_file, attach_path)
    else:
        attach_path = attach_path_old 
        attach_file = attach_file_old
        print("file X")
        
    cnt = MyDaoBoard().myupdate(board_seq, board_title, board_content, attach_file, attach_path, "", user_id, "", user_id)
    
    return render_template('question_modact.html',cnt=cnt,board_seq=board_seq)
######################################################

@app.route("/question_delact") # 디테일에서 게시글삭제
def board_delact():
    board_seq = request.args.get('board_seq')
    num_cmt =DaoCmt().del_boardcmt(board_seq)
    cnt = MyDaoBoard().mydelete(board_seq)
    flag_ses, mem_id = getSession()
    return render_template('question_delact.html', cnt=cnt,mem_id=mem_id, num_cmt=num_cmt, enumerate=enumerate)

@app.route('/board_del.ajax', methods=['POST']) #이미지 삭제
def board_del_ajax():
    board_seq = request.form["board_seq"]
    cnt = MyDaoBoard().del_img(board_seq)
    
    msg =""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"

    return jsonify(msg = msg)

@app.route('/question_detail') #질문/건의 디테일 yj 이부분수정
def question_detail():
    flag_ses, mem_id = getSession()
 
    board_seq = request.args.get('board_seq')
    obj = MyDaoBoard().myselect(board_seq)
    list = DaoCmt().select_list(board_seq)
    
    print('obj : ',obj['attach_file'])
    
    return render_template('question_detail.html', board = obj, enumerate=enumerate, mem_id= mem_id, list =list)

##################################################yj.test 댓글 
@app.route('/cmt_add.ajax', methods=['POST'])
def reply_add_ajax():
    
    cmt_content = request.form["cmt_content"]
    cmt_content = cmt_content.replace('\n','<br/>')

    in_user_id = "admin"
    board_seq = request.form["board_seq"]

    cnt = DaoCmt().insert(cmt_content, in_user_id, board_seq)
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"

    return jsonify(msg=msg)

@app.route('/cmt_del.ajax', methods=['POST'])
def reply_del_ajax():
    
    cmt_seq = request.form["cmt_seq"]
    board_seq = request.form["board_seq"]

    cnt = DaoCmt().delete(cmt_seq, board_seq)
    
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"

    return jsonify(msg=msg)

#########################################
@app.route('/set_view') #관리화면메인(그래프 등록)
def set_view():
    list = DaoGraph().counter()
    list2 = DaoVisit().counter()
    list3 = MyDaonotice().counter()
    list4 = MyDaoBoard().counter()
    
    return render_template('set_view.html', list4=list4, list3=list3, list2=list2, list=list, enumerate=enumerate)

##########################################
@app.route('/self_check_list') #맞춤법 검사 페이지
def self_check_list():
    return render_template('self_check_list.html')        

##########################################
@app.route('/self_check_money2') #연봉계싼기 페이지
def self_check_money2():
    return render_template('self_check_money2.html')

##########################################
@app.route('/kakao_map') #카카오 지도 추가
def kakao_map():
    return render_template('kakao_map.html')   

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5003)
    
    