#encapsulation is mainly for data security we can secure data by access modifiers  and we have 3 types modifiers
#public,protected and private
#public)var=100(it can access with in class and with in inherted class and main programme)
#protected)_var=100(it can access with in class and with in inherted class and main programme)
#public)__var100(it can access only inside the class)
#encapusalation can be implemented in tw0 levels  i.e mthod level and variable level
#variable level:
class  level:#public
    var=100
    def ar(self):
        print(level.var)#within class
class enc(level):
    def arc(self):
        print(level.var)#inherted class
obj=enc()
obj.arc()
print(level.var)#main programme
class encup:#protected
    _var=200
    def ar(self):#with in class
        print(encup._var)
class oops(encup):#with in inherted clss
    def arc(self):
        print(encup._var)
obj1=oops()
obj1.arc()
print(encup._var)#in main programme
class jai:#public method
    __var=300
    def ar(self):#we can access within class
        print(jai.__var)
#class ballayya(jai):#we cant access inherted class
    #def arc(self):
     #   print(jai.__var)
#obj3=ballayya()
#obj3.arc()
#print(jai.__var)#we can't access with in main programme
# we can access private variable by using method in main programme
class oops:
    __var=300
    def ar(self):
        print(oops.__var)
obj=oops()
obj.ar()#in this method having private variable we are accessing that variable in main programme by using public method
#we can change the private variable value
class python:
    __var=100
    def oops(self):
        print(python.__var)
        python__user=a
        print(python__user)
a=input("enter id:")
obj=python()
obj.oops()
#method level in this we have three access modifiers public and protected and private
#here we writed only private
class python:#in this we created private variable and private method we can access private method by using duplicate method only
    __user="teja"
    def __m1(self):
        print(python.__user)
    def d(self):
        self.__m1()
obj=python()
obj.d()


