

class Engine:
    def start(self):
        print("engiene start")

class Car:
    def __init__(self):
        self.engine=Engine()

my_car=Car()
my_car.engine.start()


class Dog:
    def __init__(self,name):
        self.name=name

    def bark(self):
        print(f"sounds woof")
my_dog=Dog('puppy')
my_dog.bark()


class Animal:
    def __init__(self,name):
        self.name=name
        pass
    def speak(self,name):
         pass

class Dog(Animal):
    def speak(self):
        print(f"{self.name} woof!")

my_dog=Dog('jhon')
my_dog.speak()

dict_comphrensions=[ ( i , i+2) for i in range(5)]
print(dict_comphrensions)


list_comphrension=[i for i in range(0,5)]
print(list_comphrension)


x=list(zip(range(5),range(2,7)))
print(x)
# x = list(zip(range(5), range(2, 7)))
# print(x)
