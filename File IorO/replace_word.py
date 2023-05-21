with open("donkey.txt",'r') as f:
    content = f.read()
content = content.replace("donkey","$$$$$")

with open("donkey.txt",'w') as f:
    content = f.write(content)