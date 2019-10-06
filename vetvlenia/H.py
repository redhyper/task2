d, m = map(int, input().split())
if m == 3 or m == 11:
    km = 1
elif m == 6:
    km = 2
elif m == 9 or m == 12:
    km = 3
elif m == 1 or m == 4 or m == 7:
    km = 4
elif m == 10:
    km = 5
elif m == 5:
    km = 6
elif m == 2 or m == 8:
    km = 0

dn = (d + km + 0) % 7
if dn == 6:
    print('Saturday')
elif dn == 0:
    print('Sunday')
elif dn == 1:
    print('Monday')
elif dn == 2:
    print('Tuesday')
elif dn == 3:
    print('Wednesday')
elif dn == 4:
    print('Thursday')
elif dn == 5:
    print('Friday')

