#one class method access in  another method is called inheritence  and they lock like two individually and physically differnet but virtually same class
#getting one class properties into anthoer class  and extablish relationship between two classes is called inheritence
#ex:classb inherting all properties of classa  and by classb we can access all properties of class a
#then a class is called parent or superclass or base class or old class
#class b is called child class or subclass or derived class or new class
#when we give any prasentation we have use terms like base and derived classes
#the major advantage of inheritence is reusability
#any class inherting by defualt object class
class a(object):#by defualt any class inherting from object class if u give object or not it will accept
    def a1(self):
        print("a1")
class b(a):
    def b1(self):
        print("b1")
obj=b()#we can call this object as instance here object is differ from class object
obj.b1()
obj.a1()#without creating object we can access a properties by using b bcz bis inherting all the properties from a so we can access direcctly
a().a1()#by using a class we can call directly
#inheritence classified into 5 types
#1)simple inheritence:one parent class properties inhertent to only one child class is called simple inheritence
class parent:
    def a1(self,a,b):#parameterized method
        c=a+b
        print(c)
    def a2(self):
        i=10
        s=0
        for i in range(1,10):
            s=s+i
            i=i+1
        print(s)
class child(parent):#relation established between parent class and child class
    def __init__(self):
        print("this is teja constructer")
    def b1(self):
        b=int(input("enter age of persons:"))
        if b>=18:
            print("ur eiligible for voting")
        else:
            print("ur age is not 18 after compliting 18 come and check")
obj=child()
obj.b1()
obj.a2()
obj.a1(10,20)#here by using child class object we accessed parent class methods
#2)multilevel inheritence:one parent class is inhertent to child class and that child class inhertent to grandchild by using grandchild object we can access parent and child methods
class parent():
    def __init__(self):
        print("this is my first constucter")
    def __init__(self):
        print("this is my second constucter")
    def a1(self):
        l=[]
        l.append(100)
        l.extend([200,300,400])
        print(l)
class child(parent):
    def __init__(self,a,b):
        print(a)
        print(b)
        print(a+b)
    def b1(self):
        a=input("enter one number:")
        i=1
        for i in range(1,11):
            print(a+"*"+str(i)+"=",int(a)*i)
class gc(child):
    def __init__(self):
        print("this is  my last constructer")

    def c1(self):
        print(list(range(1,10,1)))
obj=gc()#we can access parent and child properties from gc by using gc object
obj.c1()
obj.b1()
obj.a1()
obj1=child(10,20)#here once again iam creating obj so it defentely print constcucter if u print direct child obj it will print child constructer not gc constructer
obj1.b1()
obj1.a1()#by using child class we can access the parent clss bcz parent class is inherted to child class
obj2=parent()#here iam creating one more object for parent so it will print latest constrc=ucter
obj2.a1()
#whenever we creating any object it will print local constructer(first it will check in latest class if there is no constuctuer it will go for next parent one if there is any
#is any constructer it will print if there is no constructer it will go to next parent class and check in that class if there is any constructer it will print if there is no constucter leave it)
#3)hiearachical inheritence:in this one parent class inhertent to number of child classes
class parent():
    def __init__(self):
        print("this is also one constucter")
    def __int__(self):
        print("this is from parent class" )
    def a1(self,*args):
        print(args)
class child1(parent):
    def __init__(self):
        print("this is from child1 class")
        print("hello guys")
    def b1(self):
        b=input("enter first person name:")
        c=input("enter second person name:")
        print("hii goodmorning",b)
        print("hii goodmorning",c)
        ch=input("tell me b and c are frinds say yes or no")
        if ch=="yes":
            print(b,c,"they are friends")
        else:
            print(b,c,"they are not friends")
class child2(parent):
    def __init__(self):
        print("this is form child2 class")
        print("good evening guys")
    def c1(self):
        num = int(input("enter one number:"))
        i = 1
        c = 0
        while i <= num:
            if num % i == 0:
                c = c + 1
            i = i + 1
        if c == 2:
            print("prime")
        else:
            print("not prime")
class child3(parent):
    def __init__(self):
        print("this is from child3 class")
    def d1(self):
        t=int(input("enter any number"))
        i=2
        while i<=10:
            j=2
            while j<=t:
                print(j,"*",i,"=",i*j,end=" " )
                j=j+1
            print()
            i=i+1

obj=child3()#it will check local class if there is no constucter then it will check next parent if there is constucter it will print
obj.d1()
obj.a1(2,3,4)
obj1=parent()
obj2=child2()#this class parent class is parent
obj2.c1()
obj2.a1(10,20)
obj3=child1()#this class parent class is parent
obj3.b1()
#4)multiple inheritence:in this two parent classes inheritent to one child class
#in child class if there is same method it will give to first preference to first parent class and second prefernce to second paent class
#it will chech by order like(p1,p2) p1 is the first parent and p2 is the second parent if u give(p2,p1)then p2 is the first parent and p1 is the second parent
#in another programming languages geting diamond problem this type of solution
class stu():
    def studetails(self):
        self.name = input("ENTER NAME:")
        self.id = int(input("ENTER ID NUMBER:"))
        self.age = int(input("ENTER AGE:"))
        self.loc = input("ENTER LOCATION:")
        self.fname = input("ENTER FATHER NAME:")
        self.sclass = int(input("ENTER CLASS OF STUDENT:"))
        self.engmrks = int(input("ENTER ENGLISH MARKS:"))
        self.mathsmrks = int(input("ENTER MATHS MARKS:"))
        self.scemrks = int(input("ENTER SCIENCE MARKS:"))
        self.scal()

    def scal(self):
        self.total = self.engmrks + self.mathsmrks + self.scemrks
        self.avg = self.total / 3
        self.grade = "a+" if self.avg > 95 else "a" if self.avg <= 95 and self.avg > 90 else (
            "b" if self.avg <= 90 and self.avg > 80 else "c")
        self.display()

    def display(self):
        print("NAME=", self.name)
        print("ID=", self.id)
        print("AGE=", self.age)
        print("LOCATION=", self.loc)
        print("FATHERNAME=", self.fname)
        print("CLASS=", self.sclass)
        print("ENGLISH MARKS=", self.engmrks)
        print("MATHS MARKS=", self.mathsmrks)
        print("SCIENCE MARKS=", self.scemrks)
        print("TOTAL=", self.total)
        print("AVERAGE=", self.avg)
        print("GRADE=", self.grade)

class emp():
    def empdetails(self):
        self.name = input("ENTER NAME:")
        self.id = int(input("ENTER ID NUMBER:"))
        self.age = int(input("ENTER AGE:"))
        self.loc = input("ENTER LOCATION:")
        self.fname = input("ENTER FATHER NAME:")
        self.dsg=input("ENTER EMPLOYEE DESIGNATION:")
        self.exp=int(input("ENTER EMPLOYEE EXPERIENCE:"))
        self.sal=int(input("ENTER EMPLOYEE SALARY:"))
        self.empcal()
    def empcal(self):
        a = self.dsg
        b = self.exp
        c = self.sal
        if b >= 10:
            if a == "pm":
                hike = 0.1
                hikesalary = c + (c * hike)
            elif a == "tm":
                hike = 0.07
                hikesalary = c + (c * hike)
            elif a == "dev":
                hike = 0.05
                hikesalary = c + (c * hike)
            else:
                hike = 0.03
                hikesalary = c + (c * hike)
        elif b < 10 and b >= 5:
            if a == "pm":
                hike = 0.08
                hikesalary = c + (c * hike)
            elif a == "tm":
                hike = 0.05
                hikesalary = c + (c * hike)
            elif a == "dev":
                hike = 0.03
                hikesalary = c + (c * hike)
            else:
                hike = 0.02
                hikesalary = c + (c * hike)
        else:
            if a == "pm":
                hike = 0.05
                hikesalary = c + (c * hike)
            elif a == "tm":
                hike = 0.03
                hikesalary = c + (c * hike)
            elif a == "dev":
                hike = 0.02
                hikesalary = c + (c * hike)
            else:
                hike = 0.01
                hikesalary = c + (c * hike)
        self.hike=str(hike*100)+"%"
        self.totalsalary = hikesalary
        self.empdisplay()
    def empdisplay(self):
        print("NAME=",self.name)
        print("ID=",self.id)
        print("AGE=",self.age)
        print("LOCATION=",self.loc)
        print("FATHERNAME=",self.fname)
        print("DESIGNATION=",self.dsg)
        print("EXPERIENCE=",self.exp)
        print("SALARY=",self.sal)
        print("HIKE=",self.hike)
        print("TOTALSALARY=",self.totalsalary)
class chioce(stu,emp):
    def ch(self):
        ch=input("TELL ME WHICH ONE WANTS TO PRINT (STUDENT DETAILES OR EMPLOYEE DETAILES):")
        if ch.lower()=="studentdetails":
            self.studetails()
        else:
            self.empdetails()

obj=chioce()
obj.ch()
#5)hybrid:adding any two inheritence (human,stu,emp)is considered as hiearachical inheritence and (stu,emp chiose) as considered as multiple inheritence
class human:
    def input(self):
        self.name=input("ENTER NAME:")
        self.id=int(input("ENTER ID NUMBER:"))
        self.age=int(input("ENTER AGE:"))
        self.loc=input("ENTER LOCATION:")
        self.fname=input("ENTER FATHER NAME:")
class stu(human):
    def studetails(self):
        self.input()
        self.sclass = int(input("ENTER CLASS OF STUDENT:"))
        self.engmrks = int(input("ENTER ENGLISH MARKS:"))
        self.mathsmrks = int(input("ENTER MATHS MARKS:"))
        self.scemrks = int(input("ENTER SCIENCE MARKS:"))
        self.scal()

    def scal(self):
        self.total = self.engmrks + self.mathsmrks + self.scemrks
        self.avg = self.total / 3
        self.grade = "a+" if self.avg > 95 else "a" if self.avg <= 95 and self.avg > 90 else (
            "b" if self.avg <= 90 and self.avg > 80 else "c")
        self.display()

    def display(self):
        print("NAME=", self.name)
        print("ID=", self.id)
        print("AGE=", self.age)
        print("LOCATION=", self.loc)
        print("FATHERNAME=", self.fname)
        print("CLASS=", self.sclass)
        print("ENGLISH MARKS=", self.engmrks)
        print("MATHS MARKS=", self.mathsmrks)
        print("SCIENCE MARKS=", self.scemrks)
        print("TOTAL=", self.total)
        print("AVERAGE=", self.avg)
        print("GRADE=", self.grade)

class emp(human):
    def empdetails(self):
        self.input()
        self.dsg=input("ENTER EMPLOYEE DESIGNATION:")
        self.exp=int(input("ENTER EMPLOYEE EXPERIENCE:"))
        self.sal=int(input("ENTER EMPLOYEE SALARY:"))
        self.empcal()
    def empcal(self):
        a = self.dsg
        b = self.exp
        c = self.sal
        if b >= 10:
            if a == "pm":
                hike = 0.1
                hikesalary = c + (c * hike)
            elif a == "tm":
                hike = 0.07
                hikesalary = c + (c * hike)
            elif a == "dev":
                hike = 0.05
                hikesalary = c + (c * hike)
            else:
                hike = 0.03
                hikesalary = c + (c * hike)
        elif b < 10 and b >= 5:
            if a == "pm":
                hike = 0.08
                hikesalary = c + (c * hike)
            elif a == "tm":
                hike = 0.05
                hikesalary = c + (c * hike)
            elif a == "dev":
                hike = 0.03
                hikesalary = c + (c * hike)
            else:
                hike = 0.02
                hikesalary = c + (c * hike)
        else:
            if a == "pm":
                hike = 0.05
                hikesalary = c + (c * hike)
            elif a == "tm":
                hike = 0.03
                hikesalary = c + (c * hike)
            elif a == "dev":
                hike = 0.02
                hikesalary = c + (c * hike)
            else:
                hike = 0.01
                hikesalary = c + (c * hike)
        self.hike=str(hike*100)+"%"
        self.totalsalary = hikesalary
        self.empdisplay()
    def empdisplay(self):
        print("NAME=",self.name)
        print("ID=",self.id)
        print("AGE=",self.age)
        print("LOCATION=",self.loc)
        print("FATHERNAME=",self.fname)
        print("DESIGNATION=",self.dsg)
        print("EXPERIENCE=",self.exp)
        print("SALARY=",self.sal)
        print("HIKE=",self.hike)
        print("TOTALSALARY=",self.totalsalary)
class chioce(stu,emp):
    def ch(self):
        ch=input("TELL ME WHICH ONE WANTS TO PRINT (STUDENT DETAILES OR EMPLOYEE DETAILES):")
        if ch.lower()=="studentdetails":
            self.studetails()
        else:
            self.empdetails()

obj=chioce()
obj.ch()










