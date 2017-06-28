'''
Program to demonstrate the usage of:

- lists
- parsing data in list
- processing records from list
- check for validations, etc.

sample i/p data:

abhi|12|1982|python
abc|123|2082|go
def|18|1981|perl
pqr|18|1981|dksdh
abhi324|18|1981|perl

sample O/P for above data:

Records processed: 5
Valid recs: 2
Invalid recs: 3
rec#2: invalid age: 123
rec#4: invalid subject: dksdh
rec#5: invalid name: abhi324

rec#1:
Name=ABHI
Age=12
Year=1982
Subject=Python

rec#3:
Name=DEF
Age=18
Year=1981
Subject=Perl
'''


# input data
# could also be read from user or some file
data = '''abhi|12|1982|python
abc|123|2082|go
def|18|1981|perl
pqr|18|1981|dksdh
abhi324|18|1981|perl'''

invalid_recs_count = 0
output = []
recs = data.split('\n')
for i, rec in enumerate(recs):
    # pipe (|) is the char which separates out fields in a record
    name, age, year, subject = rec.split('|')
    age, year = int(age), int(year)
    
    if not name.isalpha():
        output.append("rec#" + str(i+1) + ": invalid name: " + name)
        invalid_recs_count += 1

    # check all the validations

print("Records processed:", len(recs))
print("Valid recs:", len(recs) - invalid_recs_count)
print("Invalid recs:", invalid_recs_count)
print("\n".join(output))