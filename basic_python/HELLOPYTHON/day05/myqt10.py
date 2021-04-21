import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from tkinter import messagebox 

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("myqt10.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        global text
        self.pb0.clicked.connect(self.pbFunction)
        self.pb1.clicked.connect(self.pbFunction)
        self.pb2.clicked.connect(self.pbFunction)
        self.pb3.clicked.connect(self.pbFunction)
        self.pb4.clicked.connect(self.pbFunction)
        self.pb5.clicked.connect(self.pbFunction)
        self.pb6.clicked.connect(self.pbFunction)
        self.pb7.clicked.connect(self.pbFunction)
        self.pb8.clicked.connect(self.pbFunction)
        self.pb9.clicked.connect(self.pbFunction)
        self.pb_call.clicked.connect(self.pbFunction_call)
        
        #전화번호누르기
    def pbFunction(self):
        
        old = self.le.text()
        text = self.sender().text()
        text = old+text
                
        self.le.setText(text)
        
    def pbFunction_call(self):
        a = self.le.text()
        #messagebox.showinfo("calling",a)
        
        QMessageBox.about(self, "calling",a)
        

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()