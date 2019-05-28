def is_prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
                break
        else:
            return True
    else:
        return False
min,max=list(map(int,input().split()))
for i in range(min+1,max):
    if is_prime(i):
        print(i,end=" ")
