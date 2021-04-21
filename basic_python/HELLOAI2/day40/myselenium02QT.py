from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("send.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.driver = webdriver.Chrome('./chromedriver') #또는 chromedriver.exe
        self.driver.get('http://127.0.0.1:5000/')
 
        self.driver.find_elements_by_tag_name('a')[3].click()
  
        self.driver.find_element_by_name('emp_id').send_keys('s00001')
        self.driver.find_element_by_id('pwd').send_keys('1')
        
        self.driver.find_elements_by_tag_name('input')[2].click()
        
        self.pb.clicked.connect(self.pbFunction)
    
        
    def pbFunction(self):  
        self.driver.find_elements_by_tag_name('a')[2].click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/table/tbody/tr[2]/td[5]/a').click()
        
        obj_table = self.driver.find_element_by_css_selector('body > table > tbody > tr > td:nth-child(1) > table')
        print(obj_table.text)
            

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
 