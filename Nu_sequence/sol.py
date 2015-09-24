a = [int(i) for i in raw_input().split()]
K = a[0]
a = a[1:]
b = [[] for i in range(K+1)]
b[0] = a[:]
for i in range(1,K+1):
    count = 1
    for j in range(1, len(b[i-1])):
        if b[i-1][j] == b[i-1][j-1]:
            count += 1
        else:
            b[i].extend([count, b[i-1][j-1]])
            count = 1
    b[i].extend([count,b[i-1][-1]])
length = [sum(len(str(k)) for k in b[i])+len(b[i])-1 for i in range(K+1)]
m = max(length)
for i in range(K+1):
    rest = m-length[i]
    one_more = (m-length[i]) % 2
    print '.'*(rest/2+one_more)+str(b[i])[1:-1].replace(',','')+'.'*(rest/2)
print len(b[K])
