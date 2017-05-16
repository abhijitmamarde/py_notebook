data="""id,fname,lname,age,dob,salary
1,abhi,jit,34,01-01-1980,100
2,aabhi,jit2,35,01-01-1981,200
13,aaabhi,jit3,36,01-01-1980,300
4,aaaaabhi,jit4,37,01-01-1981,400"""


data2=[data.split('\n')[0]]

dict_data = {}

lines = data.split("\n")

for rec in lines[1:]:
    fields = rec.split(',')
    dob = fields[4]
    salary= int(fields[5])
    print(dob, salary)
    if dob not in dict_data:
        dict_data[dob] = 0
    dict_data[dob] += salary

print(dict_data)
print('\n'.join(data2))