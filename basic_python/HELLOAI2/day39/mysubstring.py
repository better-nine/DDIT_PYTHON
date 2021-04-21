txt = '00hr0jy9999999999999999999903,00rh002'

arr = txt.split(",")

for i in arr :
    a = i[:-1]
    b = i[-1:]
    print(a, b)



