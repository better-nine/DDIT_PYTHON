import logging


class MyLog:
    def getLogger(self):
        #날짜포맷입력기
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        #로거이름
        logger = logging.getLogger('simple_example')
        #로그레벨
        logger.setLevel(logging.DEBUG)
        
        # Check handler exists
        if len(logger.handlers) > 0:
            return logger # Logger already exists

        #콘솔
        cn = logging.StreamHandler()
        logger.addHandler(cn)
        cn.setFormatter(formatter)
    
        #로그파일
        fh = logging.FileHandler(filename="MyLog.log")
        logger.addHandler(fh)
        fh.setFormatter(formatter)
    
        return logger  