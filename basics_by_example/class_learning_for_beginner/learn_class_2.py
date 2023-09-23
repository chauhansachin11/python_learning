class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def updateAge(self, age):
        self.age = age

    def compareAge(self, other):
        if(self.age == other.age):
            return True
        else:
            return False


p1 = Person("Sachin", 20)
p1.updateAge(28)

print(p1.age)
p2 = Person('Mukul', 22)
print(p2.name)

if(p1.compareAge(p2)):
    print("Have same Age")
else:
    print("Don't have same Age")