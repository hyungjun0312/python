t = 1
while(t <= 1000):
    try:
        t += 1
        n, s = map(str, input().split())

        n = int(n)

        for i in s:
            print(i*n,end='')

        print()
    except:
        t += 1
        continue