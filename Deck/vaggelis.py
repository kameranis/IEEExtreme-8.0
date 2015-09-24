def get_points(a, b):
    points = {'A':20,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':15,'Q':15,'K':15,'R':50}
    if a == 'R':
        return points[b]
    elif b == 'R':
        return points[a]
    elif a == b:
        return points[a]
    else:
        return 0

def f(a,b,i,j,N,hand):
    if i>=N or j>=N:
        return (hand,0)
    if hand[i][j] != -1:
        return (hand,hand[i][j])
    else:
        (hand,k) = f(a,b,i+1,j,N,hand)
        (hand,l) = f(a,b,i,j+1,N,hand)
        (hand,m) = f(a,b,i+1,j+1,N,hand)
        hand[i][j] = max(k,l,get_points(a[i],b[j])+m)
        return (hand, hand[i][j])

N = int(raw_input())
while N != 0:
    a = raw_input().split()
    a[-1]=a[-1][:1]
    b = raw_input().split()
    b[-1]=b[-1][:1]
    hand = [[-1]*(N) for i in xrange(N)]
    print 2*f(a,b,0,0,N,hand)[1]
    N = int(raw_input())
