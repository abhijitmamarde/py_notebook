#sum=0
i=int(input("start value:"))
e=int(input("end value:"))
sum=i
# while i<=e:
#     sum=sum+i
#     i=i+1
# print(sum)

flag =0
s=i+1
while s<=e:
    if flag ==0:
        sum=sum+s
        flag=1
    else:
        sum=sum-s
        flag=0
    s=s+1
print(sum)