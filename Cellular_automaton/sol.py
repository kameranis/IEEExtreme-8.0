import sys

def to_star(c):
    if c == '0':
        return ' '
    elif c == '1':
        return '*'
    else:
        return 'X'

[R,M,N,State] = [int(j) for j in raw_input().split()]
R = list(bin(R)[:1:-1])
R.extend(['0']*(8-len(R)))
State = list(bin(State)[2:])
State = (['0']*(N+1-len(State))) + State + ['0']
New_State = State[1:-1:]
for i in range(1,M+1):
    print '%s -%s-' % (str(i)+' '*(3-len(str(i))), ''.join(map(to_star, New_State)))
    New_State = [str(R[int(''.join(State[j-1:j+2]),2)]) for j in range(1,N+1)]
    if New_State == State[1:-1]:
        print '%s -%s-' % (str(i+1)+' '*(3-len(str(i))), ''.join(map(to_star, New_State)))
        sys.exit()
    State = ['0']+New_State+['0']

