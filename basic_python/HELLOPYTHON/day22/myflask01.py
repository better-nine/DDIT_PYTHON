from flask import Flask
import logging


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


logger = logging.getLogger('simple_example')

logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
fh = logging.FileHandler(filename="run.log")
logger.addHandler(ch)
logger.addHandler(fh)
ch.setFormatter(formatter)
fh.setFormatter(formatter)



app = Flask(__name__)

@app.route("/h1")    #url-mapping
def h1():
    sql = "11111111111111111"
    logger.debug(sql)
    #log(sql)
    return "H1"


@app.route("/h2")    #url-mapping
def h2():
    sql = "222222222222222222"
    logger.debug(sql)
    #log(sql)
    return "H2"


def log(param):
    import logging
    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.DEBUG)
    
    # 콘솔 출력을 지정합니다
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    
    # 파일 출력을 지정합니다.
    fh = logging.FileHandler(filename="run.log")
    fh.setLevel(logging.INFO)
    
    # add ch to logger
    logger.addHandler(ch)
    logger.addHandler(fh)
    
    logger.critical(param)
    logger.error(param)
    logger.warning(param)
    logger.info(param)
    logger.debug(param) 




if __name__ == "__main__":
    app.run(debug=True)
#   app.run(host='localhost', port=5000)