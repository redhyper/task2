a, b, v = map(int, input().split())
if a > b and a > v:
    print('Anton')
elif b > a and b > v:
    print('Boris')
elif v > a and v > b:
    print('Victor')
elif a == v and a > b:
    print('Boris')
elif b == v and b > a:
    print('Anton')
elif a == b and a > v:
    print('Viktor')
else:
    print('Same age')
