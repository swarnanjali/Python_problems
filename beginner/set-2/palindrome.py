number=int(input())
temp=number
new=0
while number:
    rem=number%10
    new=new*10+rem
    number//=10
if temp==new:
    print("yes")
else:
    print("no")
