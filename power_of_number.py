sum=1
num,po=list(map(int,input().split()))
while po:
    sum*=num
    po-=1
print(sum)
