#!/usr/bin/python

# Returns the area between top and bottom
def area(top, bottom, right,left):
    a = (top-bottom)*(min(right[bottom:top])-max(left[bottom:top])-1)
#    print 'bottom', bottom, 'top', top, 'area', a
    return a

def find(H,W,K,right,left):
    if K == 1:
        a = area(H,0,right,left)
#        print a,H,0
        return a
    a = [find(H-i,W,K-1,right,left)+area(H,H-i,right,left) for i in range(1,H-K+2)]
    m = max(a)
    i = a.index(m)
#    print m,H,H-i
    return m

if __name__ == '__main__':
    [H,W] = [int(i) for i in raw_input().split()]
    R = int(raw_input())
    N = int(raw_input())
    left = [-W-1]*H
    right = [W+1]*H
    for i in range(N):
        [k,l] = [int(j) for j in raw_input().split()]
        if l>0:
            right[k-1] = min(right[k-1],l)
        elif l<0:
            left[k-1] = max(left[k-1],l)
    print find(H,W,R,right,left)
