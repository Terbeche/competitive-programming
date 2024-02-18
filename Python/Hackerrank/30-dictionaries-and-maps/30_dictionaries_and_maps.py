names_number = int(input())
names_and_phones = dict()

for i in range(names_number):
    name_and_phone = input().split()
    names_and_phones[name_and_phone[0]] = name_and_phone[1]
    
try:
    while True:
        name = input()
        if name in names_and_phones:
            print(name + "=" + names_and_phones[name])
        else:
            print("Not found")
except EOFError:
    pass
