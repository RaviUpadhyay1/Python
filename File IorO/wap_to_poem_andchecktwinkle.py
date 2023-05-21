f = open('poem.txt','r')
poem = f.read()
print(poem)
if 'twinkle' in poem:
    print("\nTwinkle is present")
else:
    print("\nTwinkle is not present")
f.close()