class Car:
    wheels = 4
    doors = 2
    engine = True

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_moving = False
        self.gas = 100

    def __str__(self):
        return f'{self.make} | {self.model} | {self.year}'

    def __eq__(self, other):
        return self.make == other.make and self.model == other

    def stop(self):
        if self.is_moving:
            print('The car has been stopped')
            self.is_moving = False
        else:
            print('The car has already been stopped')

    def go(self, speed):
        if self.use_gas():
            if not self.is_moving:
                print(f'The car is going {speed}')
                self.is_moving = True
        else:
            print('You have run out of gas')
            self.stop()

    def use_gas(self):
        self.gas -= 50
        if self.gas <= 0:
            return False
        else:
            return True


class Dealership:
    def __init__(self):
        self.cars = ["Ford Fusion", "Honda Civic", "Dodge Dakota"]

    def __iter__(self):
        yield from self.cars

    def add_car(self, car):
        self.cars.append(car)


car = Car("Toyota", "Camry", 2019)
car_one = Car("Toyota", "Tundra", 2024)
car_two = Car("Toyota", "Supra", 2024)

car_three = Car("Ford", "Fusion", 2022)
car_four = Car("Honda", "Civic", 2023)
car_five = Car("Dodge", "Dakota", 2021)

my_dealership = Dealership()
my_dealership.add_car(car)
my_dealership.add_car(car_one)
my_dealership.add_car(car_two)
my_dealership.add_car(car_three)
my_dealership.add_car(car_four)
my_dealership.add_car(car_five)
car_one.doors = 4
car_one.go('fast')
car_one.use_gas()
car_one.stop()
car_two.go('slow')
car_two.use_gas()
car_two.use_gas()
car_two.stop()
if car_one == car_two:
    print('equal')
else:
    print('not equal')

print(car)
print(type(car))
print(isinstance(car, Car))
print(car_one.doors)
print(car_two.doors)
print(Car.doors)
print(f"Car one has {car_one.doors} doors.")
print(id(car_one.doors))
print(id(car_two.doors))
print(id(Car.doors))
print(dir(car_one))
print(str(car_one))

