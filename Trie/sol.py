import math

Wmax=math.floor(10**18)
Lmax=math.floor(10**5)
mul = [[] for i in range(27)]
for i in range(2,27):
    k = 1
    temp = []
    for j in xrange(int(math.ceil(math.log(Wmax,i)))+3):
        temp.append(k)
        k *= i
    mul[i] = temp[:]
print mul
N = int(raw_input())
for i in xrange(N):
    [A,L,W] = [int(j) for j in raw_input().split()]
    s = 0
    h = 0
    if A == 1:
        print (L+1)*4
        continue
    while h < L+1 and W>mul[A][h]:
        s += mul[A][h]
        h += 1
    s += W*(L+1-h)
    print s*A*4
