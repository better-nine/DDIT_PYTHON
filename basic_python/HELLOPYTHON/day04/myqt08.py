import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("myqt08.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.pbFunction)
    

    
    
    def pbFunction(self):

        # 홀짝게임 만들어야함 
        l1 = self.le1.text() #나
        #l2 = self.le2.GetText() #컴
        comran = random.randrange(1,3)
        # 1 홀 2 짝
        
        if comran==1 :
            self.le2.setText("홀")
        elif comran==2:
            self.le2.setText("짝")
            
        if l1=="짝" and comran==2 :
            self.le3.setText("이김")
        elif l1=="홀" and comran==1 :
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