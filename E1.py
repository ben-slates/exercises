def calculator(a,b):
    if user == 1:
        print(a+b)
    elif user == 2:
        print(a-b)
    elif user == 3:
        print(a*b)
    elif user == 4:
        if b == 0:
            print(f"can't divide by zero")
        else:
            print (a/b)


while True:

    print(f"Calculator\n")
    print(f"Use the Option Below to select Operation You want to perform.\n1.SUM.\n2.SUBTRACT.\n3.MULTIPLY.\n4.DIVISION. ")
    user = int(input())
    if user > 4:
        print (f"please Selct option from 1 to 4")
        break
    a = int(input(f"Enter the first Number:"))
    b = int(input(f"Enter the second Number:"))

    calculator(a,b)