'''
1. Using inheritance we can get parent class properties into child class.
'''
class A():
    name = 'SRIRAM'          # CLASS VARIABLE

    def add(self):
        print(' ADD IS : ')

    def sub(self):
        print(' SUB IS : ')

class Arth_Oper():
    def mul(self):
        print(' MUL IS : ')

    def dev(self):
        print(' DEV IS : ')

inst = Arth_Oper(A)
inst.add()
inst.sub()
inst.mul()
inst.dev()
print(inst.name)

