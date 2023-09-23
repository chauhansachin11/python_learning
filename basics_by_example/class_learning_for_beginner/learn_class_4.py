class Student:

    school = "Shri Ram"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return((self.m1+self.m2+self.m3)/3)

    def get_m1(self):
        return(self.m1)
    
    def set_m1(self, val):
        self.m1 = val

    @classmethod
    def get_schoolName(cls):
        return(cls.school)

    @staticmethod
    def info():
        print("This is Student class...")


s1 = Student(70,60,82)
s2 = Student(80,75,59)

print(s1.avg())
print(s2.avg())
print(s1.get_m1())
s1.set_m1(90)
print(s1.get_m1())

print(s1.get_schoolName())
print(Student.get_schoolName())
Student.info()

