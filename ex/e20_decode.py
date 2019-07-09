a = str()
string = input("Enter your encrypted message:\n>> ")
if string == "": #if string empty print Nothing to decode
    print("Nothing to decode")
else:
    for x in string:
        x = ord(x) #convert x to ord
        if x >= 65 and x+13 <= 103:
            x += 13
            if x > 90: #103-13 because if plus 13 more gonna be out of characters
                x -= 26
        elif x >= 97 and x+13 <= 135:
            x += 13
            if x > 122:
                x -= 26
        else:
            x = x
        a += chr(x)
    print(str(a))