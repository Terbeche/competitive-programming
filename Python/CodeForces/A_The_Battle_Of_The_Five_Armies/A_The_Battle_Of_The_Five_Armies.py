first_array = list(map(int, input().split()))
second_array = list(map(int, input().split()))


sum1 = 0
sum2 = 0

for i in range(len(first_array)):
    damage =  first_array[i] * second_array[i] 
    if i <= 2:
        sum1 += damage
    else:    
        sum2 += damage  

if sum1 > sum2:
    print("WIN")
elif sum1 < sum2:
    print("LOSE")
else:
    print("DRAW")