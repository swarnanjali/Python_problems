def bubble_sort(lis):
    l=len(lis)
    for i in range(l):
        for j in range(l-i-1):
            if lis[j]>lis[j+1]:
                lis[j],lis[j+1]=lis[j+1],lis[j]
    return lis




n=int(input())
lis=list(map(int,input().split()))
print(*bubble_sort(lis))
