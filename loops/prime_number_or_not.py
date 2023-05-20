num = int(input("Enter a number:"))
for i in range(2, num):
    if num % i == 0:
        print(num, "is not a prime number")
else:
    print(num, "is a prime number")

# Program to check if a number is prime or not
# num = int(input("Enter a number: "))
# flag = False
# if num == 1:
#     print(num, "is neither prime number nor a composite")
# elif num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             flag = True
#             break
#     if flag:
#         print(num, "is  a composite number")
#     else:
#         print(num, "is a prime number")