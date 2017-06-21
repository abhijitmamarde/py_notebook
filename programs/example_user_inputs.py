name = input("Enter name:")
age = int(input("Enter age:"))

print("name entered:", name)
print("age entered:", age)

if age >= 18:
    print("Person ", name, " is eligibile to vote.")
else:
    print("Person ", name, " is NOT eligibile to vote.")
