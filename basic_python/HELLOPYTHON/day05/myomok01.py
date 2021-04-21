from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys 
import random

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("myomok01.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.mystate = 0
        
        #self.pb.toggle()
        #self.pb.setCheckable(True)
        self.pb.clicked.connect(self.pbFunction)
        
        
    def pbFunction(self):
        if self.mystate == 0 :
            self.mystate = 1
        elif self.mystate == 1 :
            self.mystate = 2
        else :
            self.mystate = 0
        
        MyIcon = str(self.mystate)+".png"
        self.pb.setIcon(QIcon(MyIcon))
        
        #toggle = ['0.png','1.png','2.png']
        
        #if self.pb.isChecked():
        #    self.pb.setIcon(QIcon(toggle[1]))            
        #else :
        #    self.pb.setIcon(QIcon(toggle[2]))
        
        
        
       
            
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()