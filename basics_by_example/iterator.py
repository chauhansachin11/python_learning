a = [7,4,5]

it = iter(a)

print(it.__next__())
print(it.__next__())

print(next(it))

class Top10:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if(self.num <=10):
            val = self.num
            self.num +=1
            return val
        else:
            raise StopIteration


my10 = Top10()

print(next(my10))

for i in my10:
    print(i)




