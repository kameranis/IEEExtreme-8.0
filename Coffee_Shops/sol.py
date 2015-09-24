def isvalid(i,j,N,M):
    return i>=0 and i<N and j>=0 and j<M

def num_shops(i,j,shops):
    if shops[i][j] == '-':
        return 1.0
    elif shops[i][j] == 'L':
        return 2.0
    elif shops[i][j] == 'M':
        return 3.0
    elif shops[i][j] == 'H':
        return 4.0
    else:
        return 0.0

def tile_profit((i,j), coffee,shops,N,M,k):
    if isvalid(i,j,N,M):
        if shops[i][j] == 'H' and coffee[k][i][j]>=5:
            return 1
    return 0


def daily_profit(i,j,shops,coffe,N,M,k):
    tiles = [(i-1,j),(i,j+1),(i+1,j),(i,j-1)]
    return coffee[k][i][j]+sum([tile_profit(l,coffee,shops,N,M,k) for l in tiles])

def profit(i,j,shops,coffee,N,M):
    if shops[i][j] == 'H':
        return 0
    a = [daily_profit(i,j,shops,coffee,N,M,k)/num_shops(i,j,shops) for k in range(7)]
    return sum([max(a[k]-20,0) for k in range(7)])

[N,M] = [int(j) for j in raw_input().split()]
shops = [raw_input().split('*') for i in range(N)]
for i in range(N):
    shops[i][M-1] = shops[i][M-1][:1]
coffee = list()
for i in range(7):
    raw_input()
    coffee.append([[int(j) for j in raw_input().split('*')] for k in range(N)])
max_i = -1
max_j = -1
m = 0
for i in range(N):
    for j in range(M):
        p = profit(i,j,shops,coffee,N,M)
        if p > m:
            m = p
            max_i = i
            max_j = j

print max_i+1,max_j+1
