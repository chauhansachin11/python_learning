class A:
    def show(self):
        print("In A show")


class B(A):
    def show(self):
        print("In B show")



b = B()
b.show()

