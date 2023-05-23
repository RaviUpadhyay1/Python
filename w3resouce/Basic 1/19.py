# Get a new string from a given string where 'Is' has been added to the front. 
# If the given string already begins with 'Is' then return the string unchanged
text = input("Enter a text\n")
if "Is" in text:
    print(text)
else:
    print("Is" + text)