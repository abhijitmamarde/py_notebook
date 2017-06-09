'''
first_output_expected:
*
**
***
****

second_output_expected:
   *
  **
 ***
****

third_output_expected:
1
12
123
1234


Fourth program :
output_expected:
1234
123
12
1


TODO
4321
432
43
4


1234321
 23432
  343
   4


'''

print("First output using string repeatation:")
# first program
symbol = '*'
lines = 4
i = 1
while i <= lines:
    print(symbol*i)
    i += 1


print("First output:")
# first program
symbol = '*'
lines = 4
i = 1
while i <= lines:
    j = 1
    while j <= i:
        print(symbol, end="")
        j += 1
    print("")
    i += 1

print("Second output using string repeatation:")
# second program
symbol = '*'
lines = 4
i = 1
while i <= lines:
    print(" " * (lines - i), end="")
    print(symbol*i)
    i += 1

print("Second output:")
# second program
symbol = '*'
lines = 4
i = 1
while i <= lines:
    j = lines - i
    while j > 0:
        print(" ", end="")
        j -= 1
     
    j = 1
    while j <= i:
        print(symbol, end="")
        j += 1
    print("")
    i += 1


print("Third Program")
'''
third program

output_expected:
1
12
123
1234
'''

lines = 4
i = 1
while i <= lines:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print("")
    i += 1

print("Fourth Program")
'''
Fourth program :
output_expected:
1234
123
12
1
'''
i = 0
while i < lines:
    j = 1
    while j <= (lines - i):
        print(j, end="")
        j += 1
    print("")
    i += 1
