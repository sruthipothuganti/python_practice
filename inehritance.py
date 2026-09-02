"""#single inheritance
class parent:
    def fun1(self):
        print("Iam parent class")
class child(parent):
    def fun2(self):
        print("Iam child class")
d=child()
d.fun1()
d.fun2()
#multiple inheritance,multiple parent(base)class only one child(derived class)
class parent1:
    def fun1(self):
        print("Iam a parent1 class")
class parent2:
    def fun2(self):
        print("Iam a parent2 class")
class child(parent1,parent2):
    def fun3(self):
        print("Iam a child class")
c=child()
c.fun1()
c.fun2()
c.fun3()"""
#herarical inheritance (1 base(parent)class ,multiple child(derived)class)
class parent:
    def fun1(self):
        print("Iam a parent class")
class child1(parent):
    def fun2(self):
        print("Iam a child1 class")
class child2(parent):
    def fun3(self):
        print("Iam a child2 class")
class child3(parent):
    def fun4(self):
        print("Iam a child3 class")
p=child1()
p1=child2()
p2=child3()
p.fun1()
p.fun2()
p1.fun1()
p1.fun3()
p2.fun1()
p2.fun4()
#multilevel inheritance(gp(base) class,parent(derived,base) class,child(derived) class)
class gp:
    def fun1(self):
        print("Iam a grand parent class")
class parent(gp):
    def fun2(self):
        print("Iam a parent class")
class child(parent):
    def fun3(self):
        print("Iam a child class")
d=child()
d.fun1()
d.fun2()
d.fun3()