[N,M] = [int(j) for j in raw_input().split()]
a = [''.join(raw_input().split()) for i in range(N)]
pad = 2**N
errors = []
for i in range(N-1):
    temp = int(a[i],2)^int(a[i+1],2)
    if temp == 0:
        print int(a[i],2)^int(a[i+1],2)
        errors.append('i1=%d' %(i+1))
        continue
    elif not any(a[i][j]!=a[i+1][j] and a[i+1][j] == a[N-1][j] for j in range(M)):
        errors.append('i1=%d' %(i+1))
for i in range(N-2):
    for j in range(i+1,N-1):
        temp = int(a[i],2)^int(a[i+1],2)
        if not any(a[i][l]!=a[i+1][l] and a[i+1][l]==a[j][l]==a[j+1][l] for l in range(M)):
            errors.append('i1=%d i2=%d' % (i+1,j+1))

print len(errors)
for i in errors:
    print i

