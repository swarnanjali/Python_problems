h1,m1=list(map(int,input().split()))
h2,m2=list(map(int,input().split()))
minute_difference=abs((h1*60+m1)-(h2*60+m2))
hour=minute_difference//60
minute=minute_difference-(60*hour)
print(hour,minute)
