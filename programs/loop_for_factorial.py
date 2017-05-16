print("This program calculates the factorial of the number.")

n = int(input("Enter the number: "))
# c = 1
factorial = 1

for c in range(1, n+1):
    if c % 3 == 0:
        print("skiping when c is:")
        print(c)
        continue
    print("c is:")
    print(c)
    factorial = factorial * c
    print("factorial caluclated is:")
    print(factorial)
    # c = c + 1

print("The factorial of given number is:")
print(factorial)