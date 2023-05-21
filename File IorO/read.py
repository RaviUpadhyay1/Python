f = open('sample.txt')
# text = f.read() #read the all content in file
# text = f.read(5)#read the first 5 character of the file
text = f.readline() # read the single line of the content
print(text)
f.close()