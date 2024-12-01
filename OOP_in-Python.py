class Animal:
   def __init__(self,name):
    self.name=name
   def eat(self):
    print(f"{self.name} is eating ")
    return
   def sleep(self):
     print(f"{self.name} is sleeping")
     return
class Dog(Animal):
    def eat(self):
        print(f"dog {self.name} is eating")
    def bark(self):
        print(f"{self.name} is barking")
        return
class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing")
        return
    def eat(self):
        print(f"cat {self.name} is eating")

dog1=Dog("Buddy")
dog1.eat()     #Inherited from Animal and override it
dog1.bark()
cat1=Cat("Whiskers")
cat1.meow()
cat1.eat()     #Inherited from Animal and override it




