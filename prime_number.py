number=int(input())
if number>1:
    for i in range(2,number):
        if number%2==0:
            print("no")
            break
    else:
        print("yes")
else:
    print("no")
