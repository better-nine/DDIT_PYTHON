import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("myqt07.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.pb2.clicked.connect(self.pbFunction)
        self.pb3.clicked.connect(self.pbFunction)
        self.pb4.clicked.connect(self.pbFunction)
        self.pb5.clicked.connect(self.pbFunction)
        self.pb6.clicked.connect(self.pbFunction)
        self.pb7.clicked.connect(self.pbFunction)
        self.pb8.clicked.connect(self.pbFunction)
        self.pb9.clicked.connect(self.pbFunction)

    
        
    def pbFunction(self):
        #print(self.sender()) #sender() == getsource() == target()
        
        pbr = self.sender().text()
         
        pbr_int = int(pbr)
        
        result = ""
        
        for i in range(1 , 10) :
            result += str(pbr_int) + "*" + str(i) + "=" + str(pbr_int*i) + "\n"

        self.te.setText(result)
        

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()