import logging


class MyLog:
    def __init__(self):
        #날짜포맷입력기
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        #로거이름
        self.logger = logging.getLogger('simple_example')
        #로그레벨
        self.logger.setLevel(logging.DEBUG)
       
        #콘솔
        cn = logging.StreamHandler()
        self.logger.addHandler(cn)
        cn.setFormatter(self.formatter)
    
        #로그파일
        fh = logging.FileHandler(filename="MyLog.log")
        self.logger.addHandler(fh)
        fh.setFormatter(self.formatter)
     
        
    
    
    
    
    
    