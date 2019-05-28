lis_lengh=int(input())
lis=list(map(int,input().split()))
max=lis[0]
for i in lis:
    if i >max:
        max=i
print(max)
