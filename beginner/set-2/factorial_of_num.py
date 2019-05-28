num=int(input())
fact=1
if num<=1:
    print(1)
else:
    for i in range(num,0,-1):
        fact=fact*i
    print(fact)
