import random
game = True
repeat = True
user = input("Hello, what is your name?\n>> ")
count = 1
while game:
    try:
        if count == 1:
            n = random.randint(1, 88)
            num = input("Well " + user + ", try to guess the number I have in mind!\n>> ")
        if int(num) == n:
            if count == 1:
                print("You won in 1 turn only, that's amazing!")
            else:
                print("It took you " + str(count) + " turns to guess my number which was " + num + "!")
            while repeat:
                try:
                    char = input("Do you want to play again? [Y/N]\n>> ")
                    if char == 'N':
                        print("Ok, bye " + name + "! See you later!")
                        exit()
                    elif char == 'Y':
                        t = 1
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Sorry, I did not understand. Let me repeat:")
        elif 0 < int(num) < 89 and int(num) > n:
            num = input("Too high, try again!\n>>")
            count += 1
        elif 0 < int(num) < 89 and int(num) < n:
            num = input("Too low, try again!\n>> ")
            count += 1
        else:
            raise ValueError
    except ValueError:
        count += 1
        num = input("Invalid number, USAGE: 1-88, try again!\n>> ")
