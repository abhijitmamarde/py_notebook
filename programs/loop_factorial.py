print("This program calculates the factorial of the number.")

n = int(input("Enter the number: "))
c = 1
factorial = 1

while c <= n:
    print("c is:")
    print(c)
    factorial = factorial * c
    print("factorial caluclated is:")
    print(factorial)
    c = c + 1

print("The factorial of given number is:")
print(factorial)