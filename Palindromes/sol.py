def palin(a):
    if a == '':
        return 0
    i = a[::-1].index(a[0])
    if i == len(a)-1:
        return max(1,palin(a[1:]))
    return max(2+palin(a[1:-i]),palin(a[1:]))

a = raw_input()
print palin(a)
