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




num=int(input())
if is_amstrong(num):
    print("yes")
else:
    print("no")
