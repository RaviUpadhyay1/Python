letter = '''Dear <|NAME|>,
You are  selected!
I extend my gratitude to you for offering me the position of  manager in Ravi coding house.
I am delighted to accept your offer and look forward to commencing work with your company from Date : <|DATE|>.
'''
name = input("Enter your name:")
date = input("Enter date")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)