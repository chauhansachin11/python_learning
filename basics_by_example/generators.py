def top10():
    for i in range(1,11):
        yield i

def top10sq():
    n = 1

    while (n<=10):
        sq = n*n
        yield sq
        n += 1



val = top10()

print(next(val))
print(val.__next__())

for i in val:
    print(i)

valsq = top10sq()

for i in valsq:
    print(i)