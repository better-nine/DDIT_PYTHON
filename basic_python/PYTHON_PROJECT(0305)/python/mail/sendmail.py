import smtplib                              # 메일을 보내기 위한 SMTP 모듈
from email.mime.text import MIMEText

smtpName = "smtp.naver.com"                  # smtp 서버 주소
smtpPort = 587                               # smtp 포트 번호

sendEmail = "dnjohn@naver.com"
password = "9skdms94dms"



recvEmail = "940raphael@gmail.com"
title = "메일테스트보내기"                                 # 메일 제목
content = "메일내용확인하기"                                # 메일 내용

msg = MIMEText(content)                       # MIMEText(text , _charset = "utf8")
msg['From'] = sendEmail
msg['To'] = recvEmail
msg['Subject'] = title

print(msg.as_string())                        

s = smtplib.SMTP(smtpName , smtpPort)         # 메일 서버 연결
s.starttls()                                  # TLS 보안 처리
s.login(sendEmail , password)                 # 로그인
s.sendmail(sendEmail, recvEmail, msg.as_string())  # 메일 전송, 문자열로 변환하여 보냅니다.
s.close()                                     # smtp 서버 연결을 종료합니다.



def sendmail():
    
    