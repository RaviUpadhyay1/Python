j1 = int(input("Enter the liters of 1st jug: "))
j2 = int(input("Enter the liters of 2nd jug: "))
g = int(input("Enter the target liters: "))

print("x : ",j1,"\ny: ",j2,"\nTarget : ",g)
x = 0
y = 0
if  x == 0 or y == 0:
    print(x,y)
    x += j1
    print(x,y)
    if y == g:
        print("You got your desired output")
    elif y!=g:
        x = j1 - j2
        y = y + j2
        print(x,y)
        if y == g:
            print("You got your desired output")
        elif y != g:
            y = y-j2
            print(x,y)
            if y == g:
                print("You got your desired output")
            elif y != g:
                y = x
                x -= x
                print(x,y)
                if y == g:
                    print("You got your desired output")
                elif y!=g:
                    x=x+j1
                    print(x,y)
                    if y==g:
                        print("You got your desired output")
                    elif y!=g:
                        amount_needed = j2-y
                        x = x - amount_needed
                        y = y + amount_needed
                        print(x,y)
                        if y == g:
                            print("You got your desired output")
                        elif y!=g:
                            y -= y
                            print(x,y)
                            if y==g:
                                print("You got your desired output")
                            elif y!=g:
                                x,y = y,x
                                print(x,y)
                                print("You got your desired output")
else:
    print("Invalid")
