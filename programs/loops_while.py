sum = 0
ans = 'y'

while ans == 'y':
    n = int(input("Enter the number: "))
    sum = sum + n
    ans = input("Do you want to continue? (y/n): ")

print("The summation of n are: ")
print(sum)

