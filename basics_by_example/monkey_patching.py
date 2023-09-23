from power import Power

def cube(self,num):
    s = num*num*num
    print(f'The Cube of {num} = {s}')

Power.sqrt = cube
p = Power()
p.sqrt(5)