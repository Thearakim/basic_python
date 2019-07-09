import random
final_sum1 = 0
print("Welcome to dice game!")

while True:
    num = input("Enter the number of dice you want to roll:\n>> ")
    if num.isdigit():
        num = int(num)
        if num in range(1, 9):
            for i in range(1, num + 1):
                final_sum = random.randint(1, 6)
                print(f"Dice {i}: {final_sum}")
                final_sum1 = final_sum1 + final_sum
            print("=" * 10)
            print(f"TOTAL: {final_sum1}")
            print("=" * 10)
            break
        else:
            print("The number must between 1 and 8")
    else:
        print("The number must between 1 and 8")








