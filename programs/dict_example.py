# problem statement:
# program should calculate the salary of all employess on
# particular dob, 
# ex: for dob 01-01-1980 o/p shuld be 100+300=400
# ex: for dob 01-01-1981 o/p shuld be 200+400=600
data="""id,fname,lname,age,dob,salary
1,abhi,jit,34,01-01-1980,100
2,aabhi,jit2,35,01-01-1981,200
13,aaabhi,jit3,36,01-01-1980,300
4,aaaaabhi,jit4,37,01-01-1981,400"""


data2=[data.split('\n')[0]]

dict_data = {}

rows = data.split("\n")

for rec in rows[1:]:
    fields = rec.split(',')
    dob = fields[4]
    salary= int(fields[5])
    print(dob, salary)
    if dob not in dict_data:
        dict_data[dob] = 0
    # dict_data[dob] += salary
    dict_data[dob] = dict_data[dob] + salary

print(dict_data)
print('\n'.join(data2))