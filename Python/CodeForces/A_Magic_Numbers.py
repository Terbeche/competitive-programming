number  = input()

left, right = 0, 0


def magic_number(number):
    possibilities = ["144", "14", "1"]
    i = 0
    while i < len(number):
        flag = False
        for possibility in possibilities:
            if number[i:i+len(possibility)] == possibility:
                i += len(possibility)
                flag = True
                break
        if not flag:
            return False
    
    return True

if  magic_number(number):
    print("YES")
else:
    print("NO")



