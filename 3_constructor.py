## Using __init__ method we can create constructor
## Using constructor we can create instance varables.
## Constructor method will call when calling class
class One:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print(' Add a + b : ', self.a + self.b)

    def sub(self):
        print(' SUB a - b : ', self.a - self.b)

    def mul(self):
        print(' MUL a * b : ', self.a * self.b)
        
    def div (self):
        print('div a/b :',self.a/self.b)    

inst = One(300, 10)
inst.add()
inst.sub()
inst.mul()
inst.div()




