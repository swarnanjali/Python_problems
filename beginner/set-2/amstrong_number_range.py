def is_amstrong(n):
    temp=n
    l=len(str(n))
    new=0
    while n:
        rem=n%10
        new=rem**l+new
        n//=10
    if new==temp:
        return True
    else:
        return False


min,max=list(map(int,input().split()))
for num in range(min+1,max):
    if is_amstrong(num):
        print(num,end=" ")
