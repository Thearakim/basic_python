num01 = int(input("Enter a number:\n>> "))
num02 = int(input("Enter a second number:\n>> "))
if num01 > num02:
    print(f"Result : {num01} > {num02}")
elif num02 > num01:
    print(f"Result : {num02} > {num01}")
else:
    print(f"Result : {num01 } == {num02 }")
