class Student:

    def __init__(self, name, rn):
        self.name = name
        self.rn = rn
        self.lap = self.Laptop()
    
    def show(self):
        print(self.name, self.rn)

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8


s1 = Student("Sachin", 1)
s2 = Student("Raj", 2)
s1.show()
s2.show()
print(s1.lap.brand)

lap = Student.Laptop()
print(lap.cpu)