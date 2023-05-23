# Write a Python program that accepts a filename from the user and prints the extension of the file.
filename = input("Enter the filename:")
f_extension = filename.split(".")[-1]
print("The extension of the fine",f_extension)
