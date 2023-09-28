n = int(input())
petrol = []
distance = []
for i in range(n):
    a = list(map(int,input().split()))
    petrol.append(a[0])
    distance.append(a[1])
    
start_station = 0
current_station = 0
j = 0
petrol_current = 0
not_found = True
while j < n and not_found:
    if current_station == n-1:
        j = -(start_station)
    current_station = start_station + j
    petrol_current += petrol[current_station]
    petrol_current -= distance[current_station]
    if petrol_current < 0:
        start_station += 1
        j = 0
        petrol_current = 0
        continue
    if current_station == start_station - 1 and petrol_current >= 0:
        print (start_station)
        not_found = False
    j += 1
