words = ["donkey","kale","muji"]
with open("list.txt",'r') as f:
    content = f.read()
for word in words:
    content = content.replace(word,"$$$$$$")
    with open("list.txt",'w') as f:
        f.write(content)