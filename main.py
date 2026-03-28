from abc import ABC, abstractmethod
class ABC(ABC):
   def print(self,x):
        print(x)
   @abstractmethod 
   def task(self):
      print("we are inside class")
class t(ABC):
    def task(self):
        print("we are inside class t")
t=t()
t.task()
t.print(100)