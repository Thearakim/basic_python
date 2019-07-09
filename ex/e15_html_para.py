count = 0
count == 2
stlist = []
while True:
    print("Enter a string:")
    str = input()
    if str.upper()!="GEN":
        stlist.append(str)
    else:
        count = count + 1
        if count == 1:
            for i in range(0, len(stlist)):
                print(f"<p>{stlist[i]}</p>")
        elif count == 2:
            print("Nothing to display.")
            break
        else:
            break
