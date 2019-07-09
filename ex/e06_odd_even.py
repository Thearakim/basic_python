evenOdd = True
while evenOdd:
    num1 = input("Enter a number:\n>> ")
    if not num1.isdigit():
        if num1.lower() == "exit":
            break
        else:
            print(f"{num1} is not a valid number.")
    else:
        num1 = int(num1)
        if num1 % 2 == 0:
            print(f"{num1} is EVEN")
        else:
            print(f"{num1} is ODD")





