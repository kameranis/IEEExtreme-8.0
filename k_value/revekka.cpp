#include <iostream>
#include <set>
#include <cstdio>
#include <iterator>
using namespace std;
int main() {
 
    unsigned int N,M,K;
    
    if(scanf("%d %d %d", &N,&M,&K) != 3) return 2;
    int A[N];
    unsigned int i;
    
    for (i =0; i< N; i++)
    {
        if(scanf("%d", &A[i]) != 1) return 2;
    }
    multiset<int> kmin;
    for(i = 0; i < M; i++) kmin.insert(A[i]);
    while(kmin.size() > K)
        kmin.erase(--kmin.end());
    int m = *(--kmin.end());
    for (i = 0; i<N-1; i++)
    {
        if(kmin.find(A[i]) != kmin.end())
            kmin.erase(kmin.find(A[i]));
        //if(A[(i+M)%N] < m)
        {
            kmin.insert(A[(i+M)%N]);
            while(kmin.size() > K) 
                kmin.erase(--kmin.end());
            if(m > *(--kmin.end())) {
                m = *(--kmin.end());
            }
        }
    }
    printf("%d\n", m);
    
    
}
