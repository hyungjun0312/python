while(1):
    s = list(map(int, input().split()))
    if s == [0, 0, 0]:
        break
    m = max(s)
    s.remove(m)
    if m**2 == s[0]**2 + s[1]**2:
        print("right")
    else:
        print("wrong")
