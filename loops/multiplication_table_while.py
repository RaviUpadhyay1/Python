num = int(input("Enter a number:"))
i = 1
while(i<=10):
    print (num, "x", i, "=", num * i)
    i = i +1
#using concatenation
num = int(input("Enter a number:"))
i = 1
while(i<=10):
    print (str(num)+ "x"+str(i)+ "="+str(num * i))
    i = i +1