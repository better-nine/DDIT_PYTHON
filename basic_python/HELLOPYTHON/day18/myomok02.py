from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys 
import random
from tkinter import messagebox 

import cx_Oracle 

def getMax():
    connection = cx_Oracle.connect('python','python','localhost:1521/xe')
    cursor = connection.cursor()
    
    sql_str = 'select nvl(max(pan)+1,1) as maxpan from omok'
    cursor.execute(sql_str)
    max_pan=0
    for name in cursor:
        max_pan=int(name[0])
    
    return max_pan
    print("max_pan : ", max_pan)

    cursor.close()
    connection.close()


def writeHistory(pan, history, win):
    connection = cx_Oracle.connect('python','python','localhost:1521/xe')
    cursor = connection.cursor()
    
    sql_str = "insert into omok(pan, pseq, history, win) values(:1,:2,:3,:4)"
    
    
    for i, h in enumerate(history):
        cursor.execute(sql_str, (pan, i+1, h, win))
    
    connection.commit()
    cursor.close()
    connection.close()
    
    
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("myomok02.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) : #constructor 생성자
        super().__init__()
        self.setupUi(self)
        self.flag_wb = True
        self.flag_ing = True
        self.history = []
        
        self.history_arr = []
        self.all_history_arr =[]
        
        self.pb2d = []
        self.arr2d = [
                    [0,0,0,0,0, 0,0,0,0,0],
                    [0,0,0,0,0, 0,0,0,0,0],
                    [0,0,0,0,0, 0,0,0,0,0],
                    [0,0,0,0,0, 0,0,0,0,0],
                    [0,0,0,0,0, 0,0,0,0,0],
                    
                    [0,0,0,0,0, 0,0,0,0,0],
                    [0,0,0,0,0, 0,0,0,0,0],
                    [0,0,0,0,0, 0,0,0,0,0],
                    [0,0,0,0,0, 0,0,0,0,0],
                    [0,0,0,0,0, 0,0,0,0,0]]
        
        for i in range(len(self.arr2d)) : 
            line =[]      
            for j in range(len(self.arr2d)) :
                temp = QPushButton("", self)
                #temp.setText(str(i)+","+str(j))
                temp.setToolTip(str(i)+","+str(j))
                temp.clicked.connect(self.pbFunction)
                temp.setIcon(QIcon('0.png'))
                temp.setFixedSize(40,40)
                temp.setIconSize(QSize(40,40))
                temp.setGeometry(j*40, i*40, 40, 40)
                line.append(temp)
            self.pb2d.append(line)
        
        self.pb_reset.clicked.connect(self.pbreset)
        self.myrender()        


    def myrender(self): #바둑판 이미지 새로고침해주는 메서드임! 
        for i in range(len(self.arr2d)):
            for j in range(len(self.arr2d)):
                if self.arr2d[i][j] == 0 :
                    self.pb2d[i][j].setIcon(QIcon('0.png'))
                elif self.arr2d[i][j] == 1 :
                    self.pb2d[i][j].setIcon(QIcon('1.png'))
                elif self.arr2d[i][j] == 2 :                
                    self.pb2d[i][j].setIcon(QIcon('2.png'))                        
           
        
    def pbreset(self):   
        self.flag_wb = True
        self.flag_ing = True
        for i in range(len(self.arr2d)):
            for j in range(len(self.arr2d)):
                self.arr2d[i][j] = 0                
        
        self.history.clear()
        self.myrender()
        
        
    def pbFunction(self):
        if not self.flag_ing :
            return

        text = self.sender().toolTip()    
        
        arr = text.split(",") #새로운 배열이 나오기 때문에 임시로 넣어줌
        
        
        int_i = int(arr[0])
        int_j = int(arr[1])
        
        
        if self.arr2d[int_i][int_j] > 0:
            return
        
        int_stone = 0
        
        if self.flag_wb == True :
            self.arr2d[int_i][int_j] = 1
            int_stone = 1
        else :
            self.arr2d[int_i][int_j] = 2
            int_stone = 2
        
        up = self.getUP(int_i, int_j, int_stone)
        do = self.getDW(int_i, int_j, int_stone)
        le = self.getLE(int_i, int_j, int_stone)
        re = self.getRI(int_i, int_j, int_stone)

        dl = self.getDL(int_i, int_j, int_stone)
        dr = self.getDR(int_i, int_j, int_stone)
        ul = self.getUL(int_i, int_j, int_stone)
        ur = self.getUR(int_i, int_j, int_stone)
        
#         print("up:", up,"\t",end="")
#         print("down:", do,"\t",end="")
#         print("left:",le,"\t",end="")
#         print("right:",re)
#                 
#         print("leftDown:",dl,"\t",end="")
#         print("RightDown:",dr,"\t",end="")
#         print("leftUp:",ul,"\t",end="")
#         print("RightUp:",ur)
        self.myrender()
        
        str100 =""
        for i in range(len(self.arr2d)):
            for j in range(len(self.arr2d)):
                str100 += str(self.arr2d[i][j])
        
        self.history.append(str100)
        
        d1 = up + do +1
        d2 = le + re + 1
        d3 = dl + ur + 1
        d4 = ul + dr + 1
        
        #print(self.arr2d) #이게 한번 눌렀을 때의 history
        #print(self.pb2d)  
       
         
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5 :
            
            win = 0
            
            if self.flag_wb :
                QMessageBox.about(self, "Game Over", "White Win")
                win =1
         
            else :
                QMessageBox.about(self, "Game Over", "Black Win")
                win =2
            
            max_pan = getMax()
            writeHistory(max_pan,self.history,win)
            
            self.flag_ing = False
                
        self.flag_wb = not self.flag_wb #돌 색깔 바꾸는거임 
        
        
       
    def getUP(self, int_i, int_j, int_stone):    
        con = 0  
        try:    
            while True:  
                int_i += -1
              
                if int_i < 0 :
                    return con            
                
                if self.arr2d[int_i][int_j] == int_stone :
                    con += 1
                else :
                    return con
        except:
            return con
            
    def getDW(self, int_i, int_j, int_stone):    
        con = 0  
        try:    
            while True:  
                int_i += 1
              
                if int_i < 0 :
                    return con            
                
                if self.arr2d[int_i][int_j] == int_stone :
                    con += 1
                else :
                    return con
        except:
            return con
        
    def getLE(self, int_i, int_j, int_stone):    
        con = 0  
        try:    
            while True:  
                int_j += -1
              
                if int_j < 0 :
                    return con            
                
                if self.arr2d[int_i][int_j] == int_stone :
                    con += 1
                else :
                    return con
        except:
            return con
        
    def getRI(self, int_i, int_j, int_stone):    
        con = 0  
        try:    
            while True:  
                int_j += 1
              
                if int_j < 0 :
                    return con            
                
                if self.arr2d[int_i][int_j] == int_stone :
                    con += 1
                else :
                    return con
        except:
            return con
    
    #오른쪽 위 대각선    
    def getUR(self, int_i, int_j, int_stone):   
        con = 0  
        try:    
            while True:  
                int_i += -1
                int_j += 1
              
                if int_j < 0 or int_i < 0 :
                    return con            
                
                if self.arr2d[int_i][int_j] == int_stone :
                    con += 1
                else :
                    return con
        except:
            return con
    
    #왼쪽 위 대각선
    def getUL(self, int_i, int_j, int_stone):   
        con = 0  
        try:    
            while True:  
                int_i += -1
                int_j += -1
              
                if int_j < 0 or int_i < 0 :
                    return con            
                
                if self.arr2d[int_i][int_j] == int_stone :
                    con += 1
                else :
                    return con
        except:
            return con
        
    #오른쪽 아래 대각선
    def getDR(self, int_i, int_j, int_stone):   
        con = 0  
        try:    
            while True:  
                int_i += 1
                int_j += 1
              
                if int_j < 0 or int_i < 0 :
                    return con            
                
                if self.arr2d[int_i][int_j] == int_stone :
                    con += 1
                else :
                    return con
        except:
            return con
        
    #왼쪽 아래 대각선
    def getDL(self, int_i, int_j, int_stone):   
        con = 0  
        try:    
            while True:  
                int_i += 1
                int_j += -1
              
                if int_j < 0 or int_i < 0 :
                    return con            
                
                if self.arr2d[int_i][int_j] == int_stone :
                    con += 1
                else :
                    return con
        except:
            return con
        
        
        
        
        
      
      
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()