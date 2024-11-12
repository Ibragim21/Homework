class Car:
    def __init__(self,yearModel:int,make: str ,speed:int):
        self.yearModel=yearModel
        self.make=make
        self.speed=speed
    def accelerate(self):
        self.speed+=5
    def brake(self):
        self.speed-=5
car1= Car(2006,'mustang',200)
print(car1.speed)
car1.accelerate()
car1.accelerate()
car1.accelerate()
print(car1.speed)
car1.brake()
car1.brake()
car1.brake()
print(car1.speed)


# Task2
class Animal:

    def __init__(self,species:str,speed:int,weight:int,food_required:str):
        self.species=species
        self.speed=speed
        self.weight=weight
        self.food_required=food_required

    def acceleration(self):
        self.speed+=10

class Pig(Animal):

    def __init__(self,species,speed,weight,food_required,age:int):
        super().__init__(species,speed,weight,food_required)
        self.age=age

    def aging(self):
        self.age+=1

class Sheep(Animal):

    def __init__(self,species,speed,weight,food_required,wool_color:str):
        super().__init__(species,speed,weight,food_required)
        self.wool_color=wool_color

class Dog(Animal):

    def __init__(self,species,speed,weight,food_required,breed:str):
        super().__init__(species,speed,weight,food_required)
        self.breed=breed

    def weight_increase(self):
        self.weight+=5
        

dog1= Dog('Dog', 10, 25, 'Dog food', 'Goldenretriever' )
print(dog1.speed)
dog1.acceleration()
print(dog1.speed)