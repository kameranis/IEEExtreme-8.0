import sys

[start, finish,index, numbers] = [int(j) for j in raw_input().split()]
a = [input() for i in range(numbers)]
j = 0
for i in range(start, finish):
    if any([str(k) in str(i) for k in a]):
        j += 1
        if j == index:
            print i
            sys.exit()
print 'DOES NOT EXIST'
