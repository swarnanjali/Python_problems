def bubble_sort(lis):
    l=len(lis)
    for i in range(l):
        for j in range(l-i-1):
            if lis[j]>lis[j+1]:
                lis[j],lis[j+1]=lis[j+1],lis[j]
    return lis




n=int(input())
lis=list(map(int,input().split()))
sorted=bubble_sort(lis)
if n%2 !=0:
    print(lis[n//2])
else:
    print((lis[n//2]+lis[(n//2)-1])/2.0)
