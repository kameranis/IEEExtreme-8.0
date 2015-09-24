N = int(raw_input())
a = [[int(j) for j in raw_input().split()] for i in xrange(N)]
k = sum([a[i][i] for i in xrange(N)])
row = [sum(a[i]) for i in xrange(N)]
trans = [list(i) for i in zip(*a)]
col = [sum(trans[i]) for i in xrange(N)]
l = sum([a[i][N-1-i] for i in xrange(N)])
num = sum([row[i]!=k for i in xrange(N)])+sum([col[i]!=k for i in xrange(N)])+sum([l!=k])
print num
if num != 0:
    for i in xrange(N-1,-1,-1):
        if col[i] != k:
            print -i-1
    if l!=k:
        print 0
    for i in xrange(N):
        if row[i] != k:
            print i+1
