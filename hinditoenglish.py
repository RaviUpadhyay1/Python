myDict = {
    "bhada" : "utensils",
    "dabba" : "box",
    "kursi" : "chair",
    "bhada" : "fare",
    "pankha" : "fan"
}
print("Option are", myDict.keys())
a = input("Enter a Nepali word\n")
print("The meaning of your word is:", myDict.get(a))