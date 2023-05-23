# Write a Python program to test whether a passed letter is a vowel or not
# letter = input("Enter a letter\n")
# vowel = "aeiou"
# if letter in vowel:
#     print("passed letter is a vowel ")
# else:
#     print("passed letter is not a vowel")

#check word contail vowel or not?
# vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

# word = input("Enter a word")

# if any(char in vowels for char in word):
#     print('The string contains a vowel')
# else:
#     print('The string does NOT contain any vowels')

#using function
def contains_vowel(name):
    if ("a"in name or "e" in name or "i" in name or "o" in name or "u" in name):
        return "vowel"
    return "constant"
name = input("Enter a name\n")
print ("It contain a ",contains_vowel(name))
