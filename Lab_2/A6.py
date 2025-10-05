a = int(input())
h = a // 3600 % 24
mm = a % 3600 // 60
ss = a % 60
print('{}:{:02}:{:02}'.format(h, mm, ss))
