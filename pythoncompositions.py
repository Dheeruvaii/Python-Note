

class Engine:
    def start(self):
        print("engiene start")

class Car:
    def __init__(self):
        self.engine=Engine()

my_car=Car()
my_car.engine.start()



