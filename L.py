n, x, d = map(int, input().split())
posln = d * (n - 1) + x
summa = n * ((x + posln)//2)
sr = summa // n
print(sr)
