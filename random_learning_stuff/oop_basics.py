class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I dont know what to say")

class Cat(Pet):
    def speak(self):
        print("Meow")

class Dog(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old, {self.color}.")

    def speak(self):
        print("Woof")


a1 = Cat("A1", 2)
a2 = Cat("A2", 4)

a3 = Dog("A3", 4, "Brown")

a1.show()
a2.speak()
print(a3.color)
a3.show()