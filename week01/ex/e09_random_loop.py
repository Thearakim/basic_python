import random
num = input("Enter a number:\n>> ")
if num.isdigit():
    num = int(num)
    while num > 0:
        print(f"Random: {random.randint(1, 100)}")
        num -= 1
else:
    print(f"Random: {random.randrange(1, 100)}")


