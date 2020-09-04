class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Frog(Animal):
    def jump(self):
        print(f"{self.name} is jumping.")


Cat = Animal("Turtle")

Chicken = Frog("Horse")
Cat.eat()
Cat.sleep()
Chicken.sleep()
Chicken.eat()
Chicken.jump()

    