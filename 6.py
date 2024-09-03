number  = int(input("Enter yuor number:"))
n1 = number // 1000
n2 = number % 1000 //100
n3 = number % 100 // 10
n4 = number % 10
if number < 9:
    print(number)
while number >=  9:
    if number >= 1000:
        number = n1 * n2 * n3 * n4
        print(number)
    elif number >= 100:
        number =n2 * n3 * n4
        print(number)
    elif number >= 10:
        number =n3 * n4
        print(number)
    elif number == 9:
        break
    elif number < 9:
        print(number)
    n1 = number // 1000
    n2 = number % 1000 // 100
    n3 = number % 100 // 10
    n4 = number % 10







