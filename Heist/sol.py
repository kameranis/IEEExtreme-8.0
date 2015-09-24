[N,M] = [int(j) for j in raw_input().split()]
capacity = N*M
jewels = []
s = raw_input()
s = s[:-1]
while s != 'END':
    temp = s.split(',')
    temp[1] = int(temp[1])
    temp[2] = int(temp[2])
    temp.append(temp[2]*1.0/temp[1])
    jewels.append(temp)
    s = raw_input()
jewels = sorted(jewels, key = lambda k: k[3])
jewels.reverse()
i = 0
loot = []
sum_load = 0
sum_price = 0
while(i<len(jewels)):
    load = capacity/jewels[i][1]
    if load != 0:
        price = load*jewels[i][2]
        capacity = capacity%jewels[i][1]
        loot.append([jewels[i][0],load,load*jewels[i][1],price])
        sum_load += load*jewels[i][1]
        sum_price += price
    i+=1
jewels = sorted(jewels, key = lambda k: k[0])
for i in loot:
    print '%s,%d,%d,%d' % (i[0],i[1],i[2],i[3])
print '%d,%d' % (sum_load, sum_price)
print 'Each robber gets: %.2f' %(sum_price*1.0/N)
