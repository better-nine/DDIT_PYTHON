
class Dog:
    def __init__(self):
        self.bark_power = 0
        
    def learnBark(self):
        self.bark_power += 1
        
class Bird():
    def __init__(self):
        self.fly_power = 0
        self.sing_power = 0
    
    def exercise(self,fly):
        self.fly_power += fly
        

class DogBird(Dog, Bird):   #다중상속가능 
    def __init__(self):
        Bird.__init__(self)
        Dog.__init__(self)
        
    #pass    #super가 자동으로 생성됨
    #그러나 한 가지만 상속가능 / __init__을 쓸 경우는 상속문장 써줘야함 

if __name__ == '__main__':
    ds = DogBird()
    print("bark_power : " + str(ds.bark_power))
    print("fly_power : " + str(ds.fly_power))
    
    ds.learnBark()
    ds.exercise(5)
    print("-----After Experience-----")

    print("bark_power : " + str(ds.bark_power))
    print("fly_power : " + str(ds.fly_power))
    