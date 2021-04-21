from day18 import myinsert





# pan

# win 값이 없을 경우 null





def omok_insert(history, win):
          
                # pan / pseq / history / win
    #r = myinsert.fn_myinsert(history, win)
    
    hist = []
    for i in range(len(history)):
        hist += list(map(str,history[i]))
    
    his = "".join(hist)
    
    #myinsert.fn_myinsert(hist, win)
    print("argument 들어온거 : ",history)
    print("배열로 만든거 : ",hist)
    
    print("문자열로 만든거 : ",his) #이걸 백개 단위로 잘라서 배열에 넣기
    
    
    
    print("history end" , win , "승리")
























