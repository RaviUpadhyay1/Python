#jug rule
j1 = int(input("Capacity of jug 1: "))
j2 = int (input("Capacity of jug 2: "))

g = int (input("Amount of water to be measured: "))

def apply_rule(ch, x, y):
# Rule 1: Fill jug 1
    if ch == 1:
      if x<j1:
        x=j1
        return x,y
      else:
          print("Rule cannot be applied")
          return x,y

# Tranfer water j1 to j2
    elif ch == 2:
      if y<j2:
        x=x-j2
        y=j2
        return x,y
      else:
        print("Rule cannot be applier")
        return x,y
# empty j2 if it is completely filled
    elif ch == 3:
      if y==j2:
        y-=j2
        return x,y
      else:
        print("Rule cannot be applier")
        return x,y
#transfer remaining water from j1 to j2
    elif ch == 4:
      if x > 0 and y==0:
        y = x+y
        x = x-y
        return x,y
      else:
        print("Rule cannot be applier")
        return x,y
#fill j1
    elif ch == 5:
      if x < j1:
        return j1,y
      else:
        print("Rule cannot be applier")
        return x,y
# tranfer water from j1 to j2 until j2 fill
    elif ch == 6:
      if y <= j2:
        d=j2-y
        x-=d
        y+=d
        return x,y
      else:
        print("Rule cannot be applier")
        return x,y
# empty j2 if it is completely filled
    elif ch == 7:
      if x > 0 and y == j2:
        y=y-j2
        return x,y
      else:
        print("Rule cannot be applier")
        return x,y
# transfer the water from j1 to j2 and empty the j1
    elif ch == 8: 
      if x > 0 and y==0:
        y=y+x
        x-=x
        return x,y
      else:
        print("Rule cannot be applier")
        return x,y
    else:
      print("INVALID CHOICE")

x = y = 0


while(True):
  if(y==g):
    print('GOAL ACHIEVED!')
    break
  else:
    ch = int(input("Enter rule to apply: "))
    x, y = apply_rule(ch, x, y)
    print("================================STATUS===========================")
    print("CURRENT STATE:", end = " ")
    print(x, y)