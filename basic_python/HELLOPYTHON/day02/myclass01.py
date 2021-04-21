class Animal:
    def __init__(self): #constructor
        self.age = 1    #전역변수
        
    def getOld(self):    
        self.age += 1
        
    
class Human(Animal):    #상속받기는 괄호안에다 넣기
    def __init__(self):
        super().__init__()  #부모에게서 상속받는거 갖다넣는거임 
        self.power_lang = 1
    def langPowerUp(self):
        self.power_lang += 1
       
    def kwawe(self,power):
        self.power_lang += power
#   pass
    

if __name__ == '__main__': #이거 있어도 없어도 위에서부터 동작됨 
    ani = Animal()
     
    print(ani.age)
    ani.getOld()
    # print(ani.getOld()) 이건 반환값이 없어서 none로 나오는듯
    print(ani.age)
    print("=========================")
    hum = Human()
    print("사람 나이: " ,hum.age)
    hum.getOld()
    print("성장 후 사람 나이:" ,hum.age)
    print("=========================")
    print("사람 언어 레벨: " ,hum.power_lang)
    hum.langPowerUp()
    print("성장 후 사람 언어 레벨: " + str(hum.power_lang))
    hum.kwawe(5)
    print("과외 후 사람 언어 레벨: " + str(hum.power_lang))
    
    