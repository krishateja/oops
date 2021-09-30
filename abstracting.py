#abstraction:hiding implimentation to avoid showing unneccessary information
#abstraction will be implimented in two steps:class level and method level we have to create at a time
#from abc import ABC(class level),abstractmethod(methodlevel)
#from abc import *ABC(it can use for class level and method level)

from abc import ABC,abstractmethod
class sky(ABC):#class level
    @abstractmethod#method level
    def abc1(self):#in the method we can't give any implimentation
        pass

    @abstractmethod
    def abc2(self):
        pass

class child1(sky):
    def m1(self):
        print("jai balayya")


    def abc1(self):#whenever we implemented on that time we will give object bu in the above we given two abstrctmethod here we can't give object
        print(" jai balayya jai jai balayya")
class child2(child1):
    def abc2(self):#we created implimentation for first in child class here we implimented anthoer abstractmethod so we can create object
        print('jai balayya')

obj1=child2()
obj1.abc1()
obj1.abc2()
