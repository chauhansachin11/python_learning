class A:
    def feat1(self):
        print("Feat1 is working")

    def feat2(self):
        print("Feat2 is working")


class B():
    def feat3(self):
        print("Feat3 is working")

    def feat4(self):
        print("Feat4 is working")


class C(A,B):
    def __init__(self):
        print("IN C class")

a1 = C()

a1.feat1()
a1.feat2()

b1 = C()

b1.feat3()
b1.feat4()
b1.feat1()
b1.feat2()
