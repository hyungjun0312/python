N, M=map(int, input().split())
s=list(map(int, input().split()))

Max=0

for i in range(0,N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if s[i]+s[j]+s[k] <= M:
                if s[i]+s[j]+s[k] > Max:
                    Max = s[i]+s[j]+s[k]
                    
print(Max)

