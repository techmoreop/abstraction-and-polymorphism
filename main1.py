from abc import ABC, abstractmethod
class ANIMAL(ABC):
    def move(self):
        pass
class HUMAN(ANIMAL):
    def move(self):
        print("I can walk and run")
class SNAKE(ANIMAL):
    def move(self):
        print("I can crawl")
class DOG(ANIMAL):
   def move(self):
        print("I can bark ")
class lion(ANIMAL):
    def move(self):
        print("I can roar")
r = HUMAN()
r.move()
k = SNAKE()
k.move()
g = DOG()
g.move()
n = lion()
n.move()