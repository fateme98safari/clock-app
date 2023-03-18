class MyTime():
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second


    def plus(self):
        self.second += 1
        if self.second >= 60:
            self.minute +=1
            self.second -=60
        if self.minute >=60:
            self.hour += 1
            self.minute -=60

    def minus(self):
        self.second -=1
        if self.second ==0:
            self.second=60
            self.minute -=1
            
        if self.minute==0:
            self.minute=60
            self.hour-=1

    def convert_ir_to_germany(self):
        self.minute+=30
        self.hour+=2