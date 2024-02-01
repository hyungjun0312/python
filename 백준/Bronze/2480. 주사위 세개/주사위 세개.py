a, b, c=map(int,input().split())
if a==b==c:
    print(10000+a*1000)
elif (a==b and a!=c):
    print(1000+a*100)
elif (a==c and a!=b):
    print(1000+a*100)
elif (c==b and a!=c):
    print(1000+b*100)
elif (a!=b and a!=c and b!=c and a>b and a>c):
    print(a*100)
elif (a!=b and a!=c and b!=c and b>a and b>c):
    print(b*100)
elif (a!=b and a!=c and b!=c and c>b and c>a):
    print(c*100)