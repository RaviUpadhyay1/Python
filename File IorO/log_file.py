f = open("log.txt")
content = f.read()
if 'python' in content.lower():
    print("Yes python is present")
else:
    print("No python is present")
f.close()