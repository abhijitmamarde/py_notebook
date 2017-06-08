# n = 0
i = 0
# max = 20

# n = int(input("Where to start from?: "))
# max = int(input("How many numbers?: "))
# odd_or_even = input("Odd or even?(o/e): ")

n = 5
max = 19
odd_or_even = 'o'
odd_or_even_flag = 0

if odd_or_even == 'o':
    odd_or_even_flag = 1

# if n % 2 == 0:
#     print("n is even")
# else:
#     print("n is odd")

# 5(o), 20, o:
# 19*2 = 38 + 5 = 43

# 5(o), 20, e:
# 19*2 = 38 + 5 + 1 = 44

# 6(e), 20, o:
# 19*2 = (38+1) + 6 = 45

# 6(e), 20, e:
# 19*2 = 38 + 6 = 44

is_start_num_even = (n % 2 == 0)

start_value = ((max - 1) * 2) + n
if is_start_num_even and odd_or_even == 'o':
    start_value += 1
elif (is_start_num_even != True) and (odd_or_even != 'o'):
    start_value += 1    

i = start_value
while i >= n:
    if i % 2 == odd_or_even_flag:
        print(i)
    i = i - 1

