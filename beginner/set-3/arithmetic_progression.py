N,A,D=list(map(int,input().split()))
sum=0
element=A
for i in range(N):
    sum=sum+element
    element=element+D
print(sum)
    
