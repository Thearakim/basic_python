num = int(input("Enter a number: \n>> "))
num1 = int(input("Enter a second number: \n>> "))
if num > num1:
    print(f"Result : {num1} < {num}")
elif num1 > num:
    print(f"Result : {num} < {num1}")
else:
    print(f"Result : {num1} == {num}")