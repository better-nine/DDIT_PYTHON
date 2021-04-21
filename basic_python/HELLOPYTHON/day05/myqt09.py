import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("myqt09.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.pbFunction)
        
        #가위바위보
        
    def pbFunction(self):
        le1 = self.le1.text()
        
        comran = random.randrange(1,4)
        # 1 홀 2 짝
        
        if comran==1 :
            self.le2.setText("가위")
        elif comran==2:
            self.le2.setText("바위")
        elif comran==3:
            self.le2.setText("보")
            
        if le1=="가위" and comran==1 or le1=="바위" and comran==2 or le1=="보" and comran==3  :
            self.le3.setText("비김")
        elif le1=="가위" and comran==3 or le1=="바위" and comran==1 or le1=="보" and comran==2 :
            self.le3.setText("이김")
        else :
            self.le3.setText("짐")
        

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()