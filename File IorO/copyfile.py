f = open("text.txt",'r')
content = f.read()
f.close()
f = open("copy.txt",'w')
f.write(content)
f.close()
# using with
# with open("text.txt",'r') as f:
#     content = f.read()
# with open("copy.txt",'w') as f:
#     f.write(contnt)
