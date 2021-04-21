import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MyCrawler() :
    def __init__(self) :
        self.driver = webdriver.Chrome('chromedriver')
        self.driver.get('http://127.0.0.1:5000/login.html')
        self.driver.find_element_by_name('emp_id').send_keys('s00001')
        self.driver.find_element_by_id('pwd').send_keys('1')
        self.driver.find_elements_by_tag_name('input')[2].click()
        self.driver.get('http://127.0.0.1:5000/sview?survey_id=1')
        
         
    def crawl(self):
        obj_table = self.driver.find_element_by_css_selector("body > table > tbody > tr > td:nth-child(1) > table")
        obj_trs = obj_table.find_elements_by_tag_name("tr")
        for i, tr in enumerate(obj_trs):
            if i > 0:
                print(tr.find_elements_by_tag_name("td")[0].text, end="\t")
                print(tr.find_elements_by_tag_name("td")[1].text, end="\t")
                print(tr.find_elements_by_tag_name("td")[2].text, end="\t")
                print(tr.find_elements_by_tag_name("td")[3].text, end="\t")
                print(tr.find_elements_by_tag_name("td")[4].text, end="\t")
                print(tr.find_elements_by_tag_name("td")[5].text)
        

if __name__ == "__main__" :
    mc = MyCrawler()
    mc.crawl()