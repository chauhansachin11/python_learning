class Car:

    wheels = 4
    def __init__(self, ml, company):
        self.ml = ml
        self.com = company


c1 = Car(20, "Tata")
c2 = Car(15, "Mahindra")

Car.wheels = 5
print(c1.ml,c1.com, c1.wheels)
print(c2.ml,c2.com, c2.wheels)
print(Car.wheels)