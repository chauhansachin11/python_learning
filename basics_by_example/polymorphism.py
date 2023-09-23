class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyIDE:
    def execute(self):
        print("Spell Check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self, ide):
        ide.execute()


ide = PyCharm()
lap1 = Laptop()
lap1.code(ide)

ide2 = MyIDE()
lap1.code(ide2)
