#Ch_selenium/example/tutorial1.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver') #또는 chromedriver.exe
driver.implicitly_wait(1) # 묵시적 대기, 활성화를 최대 15초가지 기다린다.

# 페이지 가져오기(이동)
driver.get('http://127.0.0.1:5000/')
driver.implicitly_wait(1) 

driver.find_elements_by_tag_name('a')[3].click()
driver.implicitly_wait(1) 

#단일 element에 접근
driver.find_element_by_name('emp_id').send_keys('s00001')
driver.find_element_by_id('pwd').send_keys('1')
#driver.find_elements_by_css_selector('input[type=button]').click()
driver.find_elements_by_tag_name('input')[2].click()
driver.implicitly_wait(1) 

driver.find_elements_by_tag_name('a')[1].click()
 

for i in [2,3,4,5,6,7]:
    mem_list =  driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/table/tbody/tr['+str(i)+']/td[2]')
    mem_tel =  driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/table/tbody/tr['+str(i)+']/td[3]')
    print(mem_list.text,'\t', mem_tel.text)
  
#html = driver.page_source 
#beautiful soup 쓸 거면 위에 html 넣어주면 됨 

# 5초후 종료
#time.sleep(5)
#driver.quit() # 웹 브라우저 종료. driver.close()는 탭 종료


############################################################# 선생님이랑 한거 
objs_a = driver.find_elements_by_css_selector('a')
for i in objs_a :
    print(i.text)

obj_table = driver.find_element_by_css_selector('body > table > tbody > tr > td:nth-child(1) > table')
print(obj_table.text)

print('----------------------')
obj_trs = obj_table.find_elements_by_tag_name('tr')
for i,tr in enumerate(obj_trs):
    if i > 0 :  #0을 제외하고 출력하는 방법임 !!! 
        print(tr.find_elements_by_tag_name('td')[1].text,end="\t")
        print(tr.find_elements_by_tag_name('td')[2].text)


 