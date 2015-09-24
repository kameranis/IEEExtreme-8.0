[N,M] = [int(j) for j in raw_input().split()]
array = []
for i in range(N):
    s = raw_input().split(',')
    s[2] = int(s[2].split(':')[0])*100/(int(s[2].split(':')[0])+int(s[2].split(':')[1]))
    s.append(s[2]*(i+1))
    s.append(i)
    array.append(s)
array = sorted(array, key = lambda k : k[3]-10e-10*k[4])
array.reverse()
print array
print ''
print 'This set of heroes:'
for i in range(M):
    print array[i][0]
dictionary = {'Intelligence':0,'Strength':0,'Agility':0}
for i in range(M):
    dictionary[array[i][1]] += 1
for i in ['Intelligence','Strength','Agility']:
    dictionary[i] = dictionary[i]*100.0/M
    print 'Contains %.2f percentage of %s' % (dictionary[i], i)


