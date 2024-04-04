class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

class Duck(Animal):
    def make_sound(self):
        print("Quack!")

dog = Dog()
dog.make_sound()

cat = Cat()
cat.make_sound() 

duck = Duck()
duck.make_sound() 

class Calculator:
    def add(self, a, b=0):
        return a + b

calc = Calculator()
print("Sum:", calc.add(2, 3))  
print("Sum:", calc.add(2))    
