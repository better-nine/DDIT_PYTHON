import pandas

excel_data_df = pandas.read_excel('myexel.xlsx', sheet_name='시트1')

# print whole sheet data
print(excel_data_df)

print('-----------------------')
print(excel_data_df.columns.ravel())
print('-----------------------')
print(excel_data_df['이름'].tolist())

for i in excel_data_df.columns.ravel() :
    for n in excel_data_df[i].tolist() :
        print(n)

print('==================================================')
######################## 이하 선생님 코드 #########################################
import pandas as pd
 
# 추출 행, 열 선언
Row = 0
Column = 0
# 추출 및 변환 코드
data_pd = pd.read_excel('myexel.xlsx', 
                     header=None, index_col=None, names=None)
data_np = pd.DataFrame.to_numpy(data_pd)
# 출력
print("data_pd : \n",data_pd)
print('-----------------------')
print(data_np[Row][Column])
print('-----------------------')
for row in data_np:
    print(row[0], row[1])



