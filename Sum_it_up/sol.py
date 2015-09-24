N = int(raw_input())
a = sum([int(j) for j in raw_input().split()])
t = int(raw_input())
m = 10**9+7
for i in xrange(t):
    a = (a*2) % m
print a
