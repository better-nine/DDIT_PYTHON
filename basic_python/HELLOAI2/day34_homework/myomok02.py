import sys, random, cx_Oracle
import numpy as np
from tensorflow.keras.models import load_model
from PyQt5.QtWidgets import *
from PyQt5 import uic,QtGui,QtCore
from comtypes import com_interface_registry

def getMax():
    conn = cx_Oracle.connect('python/python@localhost:1521/xe')
    cs = conn.cursor()
    rs = cs.execute('select nvl(max(pan)+1,1) as maxpan from omok')
    max_pan = 0
    for record in rs:
        max_pan = int(record[0])
    cs.close()
    conn.close()
    return max_pan

def writeHistory(pan,history,win):
    conn = cx_Oracle.connect('python/python@localhost:1521/xe')
    cs = conn.cursor()

    sql = "insert into omok (pan,pseq,history,win) values (:1,:2,:3,:4)"
    
    for i,h in enumerate(history):         
        cs.execute(sql,(pan,i,h,win))
    
    cs.close()
    conn.commit()
    conn.close()

form_class = uic.loadUiType("myomok02.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.history = []
        self.flag_wb = True
        self.flag_ing = True
        
        self.pb2d = []
        self.arr2d = [
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],

                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                                    
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0]
        ]
        
        self.arr2d_2 = [
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],

                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                                    
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0]
        ]
        
         
        for i in range(20):
            line = []
            for j in range(20):
                temp = QPushButton("", self)
                temp.setIcon(QtGui.QIcon('0.png'))
                temp.setGeometry(j*40, i*40, 40, 40) 
                temp.setIconSize(QtCore.QSize(40,40))
                temp.setToolTip(str(i)+","+str(j))
                temp.clicked.connect(self.myclick)
                line.append(temp)
            self.pb2d.append(line)
        self.pb.clicked.connect(self.myreset)   
        self.myrender() 
            
    def myreset(self):
        self.flag_wb = True
        self.flag_ing = True
        for i in range(20):
            for j in range(20):
                self.arr2d[i][j] = 0
                
        self.history.clear()      
        self.myrender()
        
    def myrender(self):
        for i in range(20):
            for j in range(20):
                if self.arr2d[i][j] == 0:
                    self.pb2d[i][j].setIcon(QtGui.QIcon('0.png'))
                if self.arr2d[i][j] == 1:
                    self.pb2d[i][j].setIcon(QtGui.QIcon('1.png')) 
                if self.arr2d[i][j] == 2:
                    self.pb2d[i][j].setIcon(QtGui.QIcon('2.png')) 
                 
    def myclick(self):
        if not self.flag_ing :
            return
        
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        int_i = int(arr_ij[0])
        int_j = int(arr_ij[1])
        
        if self.arr2d[int_i][int_j] > 0:
            return
        
        int_stone = 0
        if self.flag_wb :
            self.arr2d[int_i][int_j] = 1
            int_stone = 1
        else:
            self.arr2d[int_i][int_j] = 2
            int_stone = 2
            
        up = self.getUP(int_i,int_j,int_stone) 
        dw = self.getDW(int_i,int_j,int_stone)   
        le = self.getLE(int_i,int_j,int_stone) 
        ri = self.getRI(int_i,int_j,int_stone)
        
        ur = self.getUR(int_i,int_j,int_stone)
        ul = self.getUL(int_i,int_j,int_stone)
        dr = self.getDR(int_i,int_j,int_stone)
        dl = self.getDL(int_i,int_j,int_stone)
        
        
        d1 = up + dw + 1
        d2 = le + ri + 1
        d3 = ur + dl + 1
        d4 = ul + dr + 1

        self.myrender()
        
        str100 = ""
        for i in range(20):
            for j in range(20):
                str100+=str(self.arr2d[i][j])
        self.history.append(str100)
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5 :
            self.flag_ing = False
            win  = 0
            if self.flag_wb :  
                QMessageBox.about(self, "omok", "백돌이 이겼습니다.") 
                win  = 1
            else :
                QMessageBox.about(self, "omok", "흑돌이 이겼습니다.") 
                win  = 2
            
            max_pan = getMax()
            writeHistory(max_pan,self.history,win)
            self.sunseo_idx = 0 
            return

        self.flag_wb = not self.flag_wb
        
        #########################################################################
                
                
        ############################################################
        model = load_model('models/20201213_202430.h5')
        w, h = 20, 20
        input_n = np.reshape(self.arr2d,(1,20,20,1))
        output = model.predict(input_n).squeeze()
        output = output.reshape((h, w))
        output_y, output_x = np.unravel_index(np.argmax(output), output.shape)   
        ############################################################..
        
        
        output_x = self.arr2d_2[1][0]
        output_y = self.arr2d_2[1][1]
         
        
            
        int_stone = 0
        if self.flag_wb :
            self.arr2d[output_x][output_y] = 1
            int_stone = 1
        else:
            self.arr2d[output_x][output_y] = 2
            int_stone = 2
            
        up = self.getUP(output_x,output_y,int_stone) 
        dw = self.getDW(output_x,output_y,int_stone)   
        le = self.getLE(output_x,output_y,int_stone) 
        ri = self.getRI(output_x,output_y,int_stone)
        
        ur = self.getUR(output_x,output_y,int_stone)
        ul = self.getUL(output_x,output_y,int_stone)
        dr = self.getDR(output_x,output_y,int_stone)
        dl = self.getDL(output_x,output_y,int_stone)
        
        d1 = up + dw + 1
        d2 = le + ri + 1
        d3 = ur + dl + 1
        d4 = ul + dr + 1

        self.myrender()
        
        str100 = ""
        for i in range(20):
            for j in range(20):
                str100+=str(self.arr2d[i][j])
        self.history.append(str100)
                
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5 :
            self.flag_ing = False
            win  = 0
            if self.flag_wb :  
                QMessageBox.about(self, "omok", "백돌이 이겼습니다.") 
                win  = 1
            else :
                QMessageBox.about(self, "omok", "흑돌이 이겼습니다.") 
                win  = 2
            
            max_pan = getMax()
            writeHistory(max_pan,self.history,win) 
            self.sunseo_idx = 0
            return

         
        self.flag_wb = not self.flag_wb    
        ################################################################################
        
        
        
    def getDL(self,int_i,int_j,int_stone):
        cnt = 0
        try:
            while True:
                int_i += +1
                int_j += -1
                if int_i < 0:
                    return cnt
                if int_j < 0:
                    return cnt
                
                if self.arr2d[int_i][int_j] == int_stone:
                    cnt += 1
                else :
                    return cnt
        except: 
            return cnt
        
    def getDR(self,int_i,int_j,int_stone):
        cnt = 0
        try:
            while True:
                int_i += +1
                int_j += +1
                if int_i < 0:
                    return cnt
                if int_j < 0:
                    return cnt
                
                if self.arr2d[int_i][int_j] == int_stone:
                    cnt += 1
                else :
                    return cnt
        except:   
            return cnt
        
    def getUL(self,int_i,int_j,int_stone):
        cnt = 0
        try:
            while True:
                int_i += -1
                int_j += -1
                if int_i < 0:
                    return cnt
                if int_j < 0:
                    return cnt
                
                if self.arr2d[int_i][int_j] == int_stone:
                    cnt += 1
                else :
                    return cnt
        except:                
            return cnt
        
    def getUR(self,int_i,int_j,int_stone):
        cnt = 0
        try:
            while True:
                int_i += -1
                int_j += 1
                if int_i < 0:
                    return cnt
                if int_j < 0:
                    return cnt
                
                if self.arr2d[int_i][int_j] == int_stone:
                    cnt += 1
                else :
                    return cnt
        except:                
            return cnt
        
    def getRI(self,int_i,int_j,int_stone):
        cnt = 0
        try:
            while True:
                int_j += 1
                if int_i < 0:
                    return cnt
                if int_j < 0:
                    return cnt
                
                if self.arr2d[int_i][int_j] == int_stone:
                    cnt += 1
                else :
                    return cnt
        except:                
            return cnt
        
    def getLE(self,int_i,int_j,int_stone):
        cnt = 0
        try:
            while True:
                int_j += -1
                if int_i < 0:
                    return cnt
                if int_j < 0:
                    return cnt
                
                if self.arr2d[int_i][int_j] == int_stone:
                    cnt += 1
                else :
                    return cnt
        except:                
            return cnt
        
    def getUP(self,int_i,int_j,int_stone):
        cnt = 0
        try:
            while True:
                int_i += -1
                if int_i < 0:
                    return cnt
                if int_j < 0:
                    return cnt
                
                if self.arr2d[int_i][int_j] == int_stone:
                    cnt += 1
                else :
                    return cnt
        except:                
            return cnt
            
    def getDW(self,int_i,int_j,int_stone):
        cnt = 0
        try:
            while True:
                int_i += +1
                if int_i < 0:
                    return cnt
                if int_j < 0:
                    return cnt
                
                if self.arr2d[int_i][int_j] == int_stone:
                    cnt += 1
                else :
                    return cnt
        except:                
            return cnt
        

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    
    
    
    
     