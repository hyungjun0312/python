n = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

t=0

for i in size:
    t+=i//T + 1
    if i%T == 0:
        t-=1

print(t)
print(n//P, n%P)