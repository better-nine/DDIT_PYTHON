
class Dog:
    def __init__(self):
        self.bark_power = 0
        
    def learnBark(self):
        self.bark_power += 1
        
class Bird(Dog):
    def __init__(self):
        super().__init__()
        #Dog.__init__(self)
        self.fly_power = 0
        self.sing_power = 0
    
    def exercise(self,fly):
        self.fly_power += fly
        
    def song(self):    
        self.sing_power += 1


if __name__ == '__main__':
    dogBird = Bird()
    
    print("bark_power: \t",dogBird.bark_power)
    print("fly_power: \t",dogBird.fly_power)
    dogBird.learnBark()
    dogBird.exercise(4)
    print("--After Experience--")
    print("bark_power: \t"+str(dogBird.bark_power))
    print("fly_power: \t"+str(dogBird.fly_power))

    