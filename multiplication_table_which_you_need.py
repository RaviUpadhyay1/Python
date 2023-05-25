
while (True):  
    i=1;  
    choice = int(input("Do you want to  printing the table press 1 otherwise press 0 for no?"))  
    if choice == 0:  
        break      
    else:
        n = int(input("Enter a number if you want  multiplication table"))
        while i<=10:
 
            print("%d X %d = %d\n"%(n,i,n*i));  
            i = i+1