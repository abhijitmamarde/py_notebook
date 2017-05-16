data="""id,fname,lname,age,dob
1,abhi,jit,34,31dec19282
2,aabhi,jit2,35,31dec19282
13,aaabhi,jit3,36,31dec19282
4,aaaaabhi,jit4,37,31dec19282"""

data = open("/Users/abhijitmamarde/input.txt").readlines()

# data2=[data.split('\n')[0]]
data2=[data[0]]

# lines = data.split("\n")
lines = data


for rec in lines[1::]:
    add_wtih = -10

    if rec.split(',')[0] == '13':
        add_wtih *= -1

    rec2="|".join(rec.split(',')[0:3] + [str(int(rec.split(',')[3])+add_wtih)] + rec.split(',')[4:])
    data2.insert(100,rec2)

print('\n'.join(data2))