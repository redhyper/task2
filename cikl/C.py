a, b = map(int, input().split())
z = b
c = a
p = 0
if b < 0:
  z = -b
if a < 0:
  c = -a
for i in range(z):
  p = p + c
if b < 0 or a < 0:
  p = -p
  print(str(a)+'*'+'('+str(b)+')'+'='+str(p))
elif b < 0 and a < 0:
  print(str(a) + '*' + str(b) + '=' + str(p))
elif b > 0 and a > 0:
  print(str(a) + '*' + str(b) + '=' + str(p))

