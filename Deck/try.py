def get_points(a, b, points):
    if a == 'R':
        return points[b]
    elif b == 'R':
        return points[a]
    elif a == b:
        return points[a]
    else:
        return 0

N = int(raw_input())
points = {'A':20,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':15,'Q':15,'K':15,'R':50}
while N != 0:
    a = raw_input().split()
    a[-1]=a[-1][:1]
    b = raw_input().split()
    b[-1]=b[-1][:1]
    hand = [[0]*(N+1) for i in xrange(N+1)]
    for i in xrange(N-1, -1,-1):
        for j in xrange(N-1, -1, -1):
            p = get_points(a[i],b[j], points)
            hand[i][j] = max(hand[i][j+1],hand[i+1][j], p+hand[i+1][j+1])
    print 2*hand[0][0]
    N = int(raw_input())
