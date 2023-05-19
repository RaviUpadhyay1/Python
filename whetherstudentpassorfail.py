sub1 = int(input("Enter a marks of Physics:"))
sub2 = int(input("Enter a marks of Chemistry:"))
sub3 = int(input("Enter a marks of Biology:"))
total = (sub1+sub2+sub3)
avg = total/3
if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail")
elif(avg<40):
    print("You are fail")
else:
    print("You are pass")