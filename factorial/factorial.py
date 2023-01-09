x = int(input("Enter a number: "))

def fact(x):
    sum = 1
    for i in range(1,x+1):
        sum = sum * i
        i += 1

    return sum

print(fact(x))