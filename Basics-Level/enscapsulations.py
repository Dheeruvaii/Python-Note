# abstractions


class Car:
    def __init__(self,make,model,year):

        self.model=model
        self.make=make
        self.year=year
        self.speed=0

        def accelerate(self,increment):
            self.speed += increment
        
        def brake(self,decrement):
            if self.speed>= decrement:
                self.speed -=decrement
            else:
                self.speed=0
        def get_speed(self):
            print(get_speed)
            return self.speed

        pass