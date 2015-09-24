N=input()
num = [int(raw_input().split()[2]) for i in range(N)]
num = list(set(num))
print num
