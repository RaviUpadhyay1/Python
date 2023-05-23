# Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string.
# Return n copies of the whole string if the length is less than 2.
def substring_copy(text, n):
    flen = 2
    if len(text) > flen:
        substring = text[:flen]
        print(n*substring)
    else:
        print(n*text)
text = input("Enter a text\n")
n = int(input("Enter a number of copies:"))
substring_copy(text, n)