# n = 0
i = 0
# max = 20

n = int(input("Where to start from?: "))
max = int(input("How many numbers?: "))
odd_or_even = input("Odd or even?(o/e): ")
odd_or_even_flag = 0

if odd_or_even == 'o':
    odd_or_even_flag = 1

# if n % 2 == 0:
#     print("n is even")
# else:
#     print("n is odd")


while i < max:
    if n % 2 == odd_or_even_flag:
        print(n)
        i = i + 1
    n = n + 1


