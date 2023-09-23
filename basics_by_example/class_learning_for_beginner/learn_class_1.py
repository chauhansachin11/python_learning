class Computer:
    def __init__(self, cpu, ram):
        self.comName = "HP Pavellian"
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is - ",self.comName,self.cpu,self.ram)


comp1 = Computer('i5', 16)
comp2 = Computer('i3', 8)

comp1.config()
comp2.config()