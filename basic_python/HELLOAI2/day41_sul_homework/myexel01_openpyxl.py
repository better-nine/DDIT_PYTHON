from openpyxl import load_workbook, Workbook 
 
load_wb = load_workbook("D:/workspace_python/HELLOAI2/day41_sul/static/upload/myexel.xlsx", data_only=True)
load_ws = load_wb['시트1']
print("-------------------------------------")
list =[]
num = 2
while load_ws['B'+str(num)].value != None :
    name = load_ws['A'+str(num)].value
    number = load_ws['B'+str(num)].value
    list.append({'name':name,'number':number})
    num += 1    
print(list)
    

for i in list:
    print(i['name'])
    print(i['number'])
    


























