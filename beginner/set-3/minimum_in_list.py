lis_lengh=int(input())
lis=list(map(int,input().split()))
min=lis[0]
for i in lis:
    if i < min:
        min=i
print(min)
