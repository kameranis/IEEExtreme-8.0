import sys

[N,M] = [int(j) for j in raw_input().split()]
tight = [set() for i in range(N+1)]
loose = [[] for i in range(N+1)]
for i in range(M):
    [a,b] = [int(j) for j in raw_input().split()]
    tight[b].add(a)
    loose[a].append(b)
solution = [int(j) for j in raw_input().split()]
for i in solution:
    if tight[i] != set():
        print 'NO'
        sys.exit()
    for j in loose[i]:
        tight[j].remove(i)
print 'YES'
