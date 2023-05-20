n = int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        # print * completely in first and last row
        # print * only in first and last position in other rows
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()