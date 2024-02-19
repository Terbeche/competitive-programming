stops_number = int(input())
 
min_capacity = 0
passengers_numbers = 0

for i in range(stops_number - 1):
    exit_passengers, enter_passengers = map(int, input().split())
    passengers_numbers = passengers_numbers - exit_passengers + enter_passengers
 
 
    min_capacity = max(min_capacity, passengers_numbers)
    
print(min_capacity)
