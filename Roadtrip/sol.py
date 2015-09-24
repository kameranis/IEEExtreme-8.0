M = int(raw_input())
cost = [0]*M
for i in range(M):
    [N,F,T,L] = [int(j) for j in raw_input().split()]
    stations = [[int(j) for j in raw_input().split()] for k in range(N)]
    stations = sorted(stations, key = lambda k: k[0])
    left = -1
    right = 0
    while(right < N and stations[right][0] <= T):
        right += 1
    if right == 0:
        print -1
        continue
    if right == N:
        print 0
        continue
    m = stations[0][1]
    k = 0
    for j in range(1,right):
        if stations[j][1] < m:
            m = stations[j][1]
            k = j
    T -= stations[k][0]
    while True:
        right = k
        while(right < N and stations[right][0]-stations[k][0] <= F):
            right += 1
        if right == k:
            print -1
            break
        if k == N-1:
            print cost[i]+(L-stations[k][0]-T)*stations[k][1]
            break
        if(stations[k+1][0]-stations[k][0] > F):
            print -1
            break
        m = stations[k+1][1]
        pos = k+1
        for j in range(k+1,right):
            if m < stations[k][1]:
                break
            if stations[j][1] < m:

                m = stations[j][1]
                pos = j
        if L-stations[k][0]<=F and m > stations[k][1]:
            print cost[i]+(L-stations[k][0]-T)*stations[k][1]
            break
        elif m >= stations[k][1]:
            cost[i] = cost[i]+(F-T)*stations[k][1]
            T = F-stations[pos][0]+stations[k][0]
            k = pos
        else:
            cost[i] += (stations[pos][0]-stations[k][0]-T)*stations[k][1]
            k = pos
            T = 0

