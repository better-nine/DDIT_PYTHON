from datetime import timedelta, datetime

 

class Counter:
    def __init__(self) :
        self.date = datetime.today().strftime("%Y%m%d")
        self.count_list = [self.date, 0]
         
     
    def count(self) :
        if self.count_list[0] == self.date :
            self.count_list[1] += 1
        else :
            self.count_list[0] = self.date
            self.count_list[1] = 0
            
        return self.count_list
