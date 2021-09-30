#assignment by using module:
#students details ,total, avg and grade:
class student:
    schname="gnanodaya high school"
    def sdatails(self):
        self.sname=input("ENTER STUDENT NAME:")
        self.sclass=input("ENTER CLASS OF STUDENT:")
        self.srollnumber=int(input("ENTER ROLLNUMER OF STUDENT"))
        self.sh=int(input("how many subject marks are u going to enter:"))
        self.smarks=input("enter student marks")

    def scalculations(self):
        a=self.smarks.split()
        print(a)
        total=0
        for i in range(len(a)):
            total=total+int(a[i])
        self.total=total
        self.avg=self.total/self.sh
        self.grade="a+" if self.avg>95 else "a" if self.avg<=95 and self.avg>90 else ("b" if self.avg<=90 and self.avg>80 else "c")
    def sdisplay(self):
        print("STUDENT SCHOOL NAME:",student.schname)
        print("STUDENT NAME:", self.sname)
        print("STUDENT CLASS:",self.sclass)
        print("STUDENT ROLLNUMBER:",self.srollnumber)
        print("STUDENTS MARKS",self.smarks)
        print("STUDENT TOTAL MARKS:",self.total)
        print("STUDENT AVERAGE:",self.avg)
        print("STUDENT GRADE:",self.grade)
        print("****THANKING YOU***")
obj=student()
obj.sdatails()
obj.scalculations()
obj.sdisplay()
#empolyee details and calculations :
class employee:
    company="kphbtrading"
    def empdetails(self):
        self.empname=input("ENTER EMPOLYEE NAME:")
        self.empid=input("ENTER EMPLOYEE ID:")
        self.empdsg=input("ENTER EMPLOYEE DESIGNATION:")
        self.salary=int(input("ENTER EMPLOYEE SALARY:"))
        self.empexp=int(input("ENTER EMPLOYEE EXPERIENCE:"))
    def empcalculations(self):
        a=self.empdsg
        b=self.empexp
        c=self.salary
        if b>=10:
            if a=="pm":
                hike=0.1
                hikesalary=c+(c*hike)
            elif a=="tm":
                hike = 0.07
                hikesalary = c + (c * hike)
            elif a=="dev":
                hike = 0.05
                hikesalary = c + (c * hike)
            else:
                hike = 0.03
                hikesalary = c + (c * hike)
        elif b<10 and b>=5:
            if a=="pm":
                hike=0.08
                hikesalary=c+(c*hike)
            elif a=="tm":
                hike = 0.05
                hikesalary = c + (c * hike)
            elif a=="dev":
                hike = 0.03
                hikesalary = c + (c * hike)
            else:
                hike = 0.02
                hikesalary = c + (c * hike)
        else:
            if a=="pm":
                hike=0.05
                hikesalary=c+(c*hike)
            elif a=="tm":
                hike = 0.03
                hikesalary = c + (c * hike)
            elif a=="dev":
                hike = 0.02
                hikesalary = c + (c * hike)
            else:
                hike = 0.01
                hikesalary = c + (c * hike)
        self.totalsalary=hikesalary
    def empdisplay(self):
        print("COMPANY NAME:",employee.company)
        print("EMPLOYEE NAME",self.empname)
        print("EMPLOYEE ID",self.empid)
        print("EMPLOYEE DESIGNATION",self.empdsg)
        print("EMPLOYEE SALARY",self.salary)
        print("EMPLOYEE EXPERIENCE",self.empexp)
        print("EMPLOYEE TOTALSALARY",self.totalsalary)
obj2=employee()
obj2.empdetails()
obj2.empcalculations()
obj2.empdisplay()


#types variables;
#local variables,instance variables and static variables
#one programme with all variables
class variables:
    a="this is variables programme"#whenever u give variable inside the class out side the methods is called static variables
    #we can access static variables with <class name> static variable is class level variable and we can use static variable
    #with is the class and in method also (in method we have to use class name)
    def b(self):
        c="we started programme on that time"#this is called local variable we can use these local variable with in the method we cant use out of the method
        self.d="thank you"#this is called instance variable we can use this variable in differet method this is called method level
        #we cant use this variable within class but we can use in different methods
        print(c)
        print(self.d)
    def c(self):
        print(variables.a)#here we are using static method by using class name
        print(self.d)#here we are using instance variable we can call instance variable as global variable method level
        print(self.a)#we can use static variable with self keyword we can access but it strongly recommended to not use cause
        #we don't know which one is instance and which one is static
    print(a)#we can use static variable anywhere with in the class but whereever you give it will print starting of the output
obj=variables()
obj.b()
obj.c()
#types of methods
#instance method,class method and static method
#intance method:
class intance:
    def inmethod(self):
#whatever we define a method with self keyword is called instance method 99%of methods are instance methods we can access instance method by useing object
        a=100
        b=200
        c=a+b
        print("this is istance method:",c)
obj=intance()
obj.inmethod()#we have only one method to acceces instance method that is by giving object
#class method:
class clmethod:
    @classmethod#anotation:whenever we give classmethod anotation it will give method with cls keyword
    def cmethod(cls):#instance variable we can't create in class method because we don't have self keyword in classmethod
        a="i'm doing python programme"# we create only local variables and we can access static variables in calssmethod by using class name
        b="with in that i'm doing types method"
        c=a+" "+b
        print("this is class method:",c)
obj1=clmethod()
obj1.cmethod()
clmethod.cmethod()#aditional advantage of class method is we can access by using class name
class smthod:
    @staticmethod #static method dosen't have any keyword
    def stmethod():
        a="teja"#we can create only local variables and we can access static variables in static methods by using class name
        b="goodboy"#we can't create instance variables
        c=a+" "+b
        print(c)
obj2=smthod()
obj2.stmethod()
smthod.stmethod()#aditional advantage of static method is we can access by using class name
#special method constructor method:__init__():or magical method
class student:
    schname = "gnanodaya high school"
    def __init__(self):
        print("hii guys")
        self.sdatails()
    def sdatails(self):
        self.sname=input("ENTER STUDENT NAME:")
        self.sclass=input("ENTER CLASS OF STUDENT:")
        self.srollnumber=int(input("ENTER ROLLNUMER OF STUDENT"))
        self.sh=int(input("how many subject marks are u going to enter:"))
        self.smarks=input("enter student marks")
        self.scalculations()

    def scalculations(self):
        a=self.smarks.split()
        print(a)
        total=0
        for i in range(len(a)):
            total=total+int(a[i])
        self.total=total
        self.avg=self.total/self.sh
        self.grade="a+" if self.avg>95 else "a" if self.avg<=95 and self.avg>90 else ("b" if self.avg<=90 and self.avg>80 else "c")
        self.sdisplay()
    def sdisplay(self):
        print("STUDENT SCHOOL NAME:",student.schname)
        print("STUDENT NAME:", self.sname)
        print("STUDENT CLASS:",self.sclass)
        print("STUDENT ROLLNUMBER:",self.srollnumber)
        print("STUDENTS MARKS",self.smarks)
        print("STUDENT TOTAL MARKS:",self.total)
        print("STUDENT AVERAGE:",self.avg)
        print("STUDENT GRADE:",self.grade)
        print("****THANKING YOU***")
obj=student()
#in one class we can create n number of nested class and each nested classes individully we can create n number of nested classes

#nested class
#by using self keyword we can access one method in another method
class outer:
#in this class constructer and a1method and class inner are the class members of class outer
    def __index__(self):
        print("this is also constructer")
    def __init__(self):#we can create n number constructers but latest one will be output
        print("this is constructer")#this is latest one so it will print in output
        self.a1()
    def a1(self):
        print("a1 from a1 method")
        obj=self.inner()#here inner is clas so we have to create object
        obj.b1()#in inner class we have method b1
        self.inner().b1()#this is another type to access inner funtion
    class inner:#method b1 is the class member of inner class
        def b1(self):
            print("b1 from b1 method")
outer()
#nested class in that  one more nested class
class outer:#in this class a1 method and inner class are mebers
    def a1(self):
        print("a1 from a1 method")
    class inner:
        def b1(self):
            print("b1 from b1 method")
        class nested:
            def c1(self):
                print("c1 from c1 method")
obj=outer()#left side of the equal is reference part and right side is object part
obj.a1()
obj1=obj.inner()
obj1.b1()
obj2=obj1.nested()
obj2.c1()
#we can access like below type(direct we can call without creating object refernce)
outer().a1()
outer().inner().b1()
outer().inner().nested().c1()
#nested method(in the method we don't have chance to create nested method but we can create function only)
class outer:
    def a1(self):#this is methid
        print("a1 from a1 method")
        def a2():#this is function without any keyword if u give any keyword it will accept as argument when we give arguments it will wait for values in calling function
            print("a2 from a2 function")
        a2()
obj=outer()
obj.a1()
#we can access by using clouser property
class outer:
    def a1(self):
        print("a1 from a1 method")
        def a2():
            print("a2 from a2 function")
        return a2
obj=outer()
a=obj.a1()
a()
#within method difining class
#first traditional method
class outer:
    def a1(self):
        print("teja is typing ")
        print("raju is practicing ")
        print("srinu is listening songs")
        class inner:
            def a2(self):
                print("vinod went to shop")
                print("chandu went to hospital")
        obj=inner()
        obj.a2()
obj=outer()
obj.a1()
#clouser property
class outer:
    def a1(self):
        print("teja is typing ")
        print("raju is practicing ")
        print("srinu is listening songs")
        class inner:
            def a2(self):
                print("vinod went to shop")
                print("chandu went to hospital")
        return inner
obj=outer()
x=obj.a1()
x().a2()
