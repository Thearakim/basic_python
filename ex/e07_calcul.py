total = 0
while True:
    str = input("Enter a number:\n>> ")
    if str == "exit":
        break
    else:
        try:
            str = int(str)
            total += str
            print(f"TOTAL: {total}")
        except:
            print(f"TOTAL: {total}")