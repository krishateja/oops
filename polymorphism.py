#polymorphism:if the same object behaves differently in different situations is called polymorphism
#poly=many,morphism=forms
#polymorphism is implementing in two ways:1)over loading and2)over riding.
#over loading will do in single class,but overriding  will do in multiple classes
#1)over loading has 4 types
#variable ,operatar,constructer and mthod overloading.
#python will not support constructer and method overloading because python have better feature
#1)VARIABLE OVERLOADING:in this method variable name given same to loacal variable, instance variable and static variable
class variable:
    a="method"#static variable name given as a
    def var(self):
        a="over"
        a="teja"#latest one will be print
        print(a)#local variable name given as same name as static variable is a
        print(variable.a)
    def able(self):
        a="variable"#here given same variable name as a
        print(a)
        print(variable.a)
obj=variable()
print(variable.a)
obj.var()
obj.able()
#variable a performs different in different situations in static variable behaves like static variable and local variable its behaves like local variable
#2)operator overloading:in this overloading one single operator behaves like different in different situations
class operator:
    def __init__(self,a,b):
        print(a+b)
#here operator + will perform different in different situation
obj=operator(10,20)#here we are passing int values it will give addition of that two numbers
obj=operator("krishna","teja")#here we are passing two string values then it will give concodination
#3)method overloading:method name will be same
#this method is not support in python y because we have new method in python to perform better then method overloading
    #1)its for other languages
#we have consider 4 steps sameclass,samemethod,different(same)signeture and different implementation
class method:
    def m1(self):
        print("method overloading")
    def m1(self,a,b):
        print(a+b)
    def m1(self,a,b):
        print(a*b)
    def m1(self,a,b,c):
        print(a+b+c)
obj=method()
obj.m1(10,20)#TypeError: m1() missing 1 required positional argument: 'c'
#in python it will execute latest one so it will required positional argument c but in differnt languages it will executed by positional arguments
#in python we sameclass,samemethodname,different signeture and different implementation
class method:
    def m1(self,*args):
        if len(args)==0:
            print("this from method overloading")
        elif len(args)==1:
            print("hiii",args[0])
        elif len(args)==2:
            print(args[0]+args[1])
        elif len(args)==3:
            m=1
            for i in args:
                m=m*i
            print(m)
        else:
            s=0
            for i in args:
                s=s+i
            print(s)
obj=method()
obj.m1()
obj.m1("balakoti")
obj.m1(10,20)
obj.m1(12,25,36)
obj.m1(14,14,14,14)
#hiii balakoti
#30
#10800
#56
#4)constructer overloading:same as method overloading
class cons:
    def __init__(self,*args):
        if len(args) == 0:
            print("this from method overloading")
        elif len(args) == 1:
            print("hiii", args[0])
        elif len(args) == 2:
            print(args[0] + args[1])
        elif len(args) == 3:
            m = 1
            for i in args:
                m = m * i
            print(m)
        else:
            s = 0
            for i in args:
                s = s + i
            print(s)
obj=cons()
obj=cons(12,25)
obj=cons("balakoti")
obj=cons(14,25,54)
obj=cons(14,14,14,14)
#overriding:overriding is implemnting in multiple classes
#overriding classified into 3 types method overloading,variable overriding and constructer overriding
#method overriding:different class,same method , same signeture,different implimentation
class a:
    def m1(self,a,b):
        print(a+b)
class b(a):
    def m1(self,a,b):
        print(a*b)
obj=b()
obj.m1(12,13)
#classa has m1 method and classb has m1 method  so it will check first local method that is classb if there is m1 method it will print otherwise it will print classa of m1 this is called overriding
#variable overriding:
class A:
    var="teja"
    def m1(self,a,b):
        print(a+b)
        print(A.var)
class B(A):
    var="krishna"
    def m1(self,a,b):
        print(a+b)
        print(B.var)
obj=B()
obj.m1(10,20)
print(obj.var)
#first it will check local class in that m1 method,variable is there it will execute then it will check parant class
#constructer overriding:
class A:
    def __init__(self):
        print("this is from first constructer")
class B(A):
    def __init__(self):
        print("this is from second constructer")

obj=B()
#classA of constructer is overriding to the classB of constructer so is called constructer overriding.


