#include <cstdio>

using namespace std;

int N;

int max(int a,int b,int c)
{
    if(a>b) {
        if(a>c) return a;
        else return c;
    }
    else {
        if(b>c) return b;
        else return c;
    }
}

int points(char a, char b)
{
    if(a == 'R') a = b;
    if(b == 'R') b = a;
    if(a == b) {
        int i;
        switch(a) {
            case 'A': i = 20; break;
            case '2': i = 2; break;
            case '3': i = 3; break;
            case '4': i = 4; break;
            case '5': i = 5; break;
            case '6': i = 6; break;
            case '7': i = 7; break;
            case '8': i = 8; break;
            case '9': i = 9; break;
            case 'T': i = 10; break;
            case 'J': i = 15; break;
            case 'Q': i = 15; break;
            case 'K': i = 15; break;
            case 'R': i = 50; break;
        }
        return i;
    }
    else return 0;

}

int f(char a[], char b[], int i, int j, int hand[], int N)
{
    if(i>=N || j>=N) return 0;
    if(hand[i*N+j] != -1) return hand[i*N+j];
    else
    {
        int k = f(a,b,i+1,j,hand,N);
        int l = f(a,b,i,j+1,hand,N);
        int m = f(a,b,i+1,j+1,hand,N);
        return max(k,l,m+points(a[i],b[j]));
    }
}


int main()
{
    scanf("%d", &N);
    while(N != 0)
    {   
        char a[N], b[N];
        for(int i = 0; i < N; i++)
        {
            a[i] = getchar();
            getchar();
        }
        getchar();
        for(int i = 0; i < N; i++)
        {
            b[i] = getchar();
            getchar();
        }
        getchar();
        int hand[N*N];
        for(int i = 0; i < N; i++)
            for(int j = 0; j < N; j++)
                hand[i*N+j] = -1;
        printf("%d\n", 2*f(a, b, 0, 0, hand, N));
        scanf("%d", &N);
    }
}

