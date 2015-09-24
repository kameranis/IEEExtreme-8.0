def hand(a,b,points):
    if a == []:
        return 0
    i = -1
    c = a[0]
    if c == 'R':
        if b != []:
            return max([points[b[i]]+hand(a[1:],b[i+1:], points) for i in xrange(len(b))])
        else:
            return 0
    if c in b:
        i = b.index(c)
    if 'R' in b:
        i = b.index('R')
    if c in b and 'R' in b:
        i = min(b.index(c), b.index('R'))
    if i != -1:
        return max(points[c]+hand(a[1:],b[i+1:], points),hand(a[1:],b, points))
    else:
        return hand(a[1:],b, points)


N = int(raw_input())
points = {'A':20,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':15,'Q':15,'K':15,'R':50}
while N != 0:
    a = raw_input().split()
    a[-1]=a[-1][:1]
    b = raw_input().split()
    b[-1]=b[-1][:1]
    print 2*hand(a,b,points)
    N = int(raw_input())
