number=int(input())
temp=number
new=0
while numer:
    rem=number%10
    new=new*10+rem
    number//=10
if temp==new:
    print("yes")
else:
    print("no")
