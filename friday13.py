import time

print(time.gmtime(1))

dayCount = [31,28,31,30,31,30,31,31,30,31,30,31]

y,m = 2005,7
seconds = int(y) * 365.25 + int(m) * 24*60*60
print(seconds)

print(time.gmtime(int(seconds)))

