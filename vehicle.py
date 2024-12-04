class Vehicle:

    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage=mileage



class Car(Vehicle) : 
    pass
car = Car("volva", 180, 30)
print( "vehicle for cars" , car.name)
print("speed of car", car.speed )
print("mileage of car " , car.mileage)