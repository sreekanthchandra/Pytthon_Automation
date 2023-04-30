'''
Using class we can create object
'''

# Craete a class with varable and methods
class One():
    name = 'sreekanth chandra'

    def add(self, a, b):
        print(' add is :', a+b)
      
    def sub(self):
        print (' sub is :')  

    def sum(self, a, b):
        return a + b

# To create a instance to the class
inst = One()

# To print class variable name
print(' Name is :', inst.name)

# To call add method
inst.add(2,3)

# To call sub method 
inst.sub()

# To call sum method
k  = inst.sum(5,6)
print(' Sum is :', k)
