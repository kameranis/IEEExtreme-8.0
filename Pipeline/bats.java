/* Bats NTUA ECE PL1 spring semester 2014
 * In a rectangle there are bats (B), walls (-) and a spider (A)
 * Using only straight lines from one bat to another, without going through a wall
 * how far is the spider from (0,0)
 *
 * 2 decimals required
 */

import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;

/* This class is used by the priority queue to determine the next one
 * in Djikstra.
 * Holds the id number of the creature and its current tentative distance
 * in respect to (0,0) */

class interest implements Comparable<interest> {
    public int id;
    public int dist;

    @Override
    public int compareTo(interest a)
    { 
        if(this.dist-a.dist!=0) return this.dist-a.dist;
        else return this.id-a.id;
    }

    @Override
    public boolean equals(Object other)
    {
        if(this == other) return true;
        if(other == null || (this.getClass() != other.getClass()))
        {
            return false;
        }
        interest guest = (interest) other;
        return (this.id == guest.id) && (this.dist == guest.dist);
    }

    /* Constructors */
    interest(int i, int d) { id = i; dist = d;}
    interest() { id = 0; dist = 0;}
}

/* Main class */
public class bats {

    static int min(int a, int b) { return a < b ? a : b; }
    static int max(int a, int b) { return a > b ? a : b; }

    public static void main(String[] args) {

        /* Input */
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int[][] point = new int[N][N];
        in.nextLine();          // Skip line feed

        /* Reading interesting point */
        for(int i = 0; i < N; i++)
        {
            for(int j = 0; j < N; j++)
            {
                int r = in.nextInt();
                point[i][j] = r;
            }
            String str = in.nextLine();
        }
        /* Initialize parameters */

        // A*: Prints the tentative distance of (0,0) to spider
        PriorityQueue<interest> queue = new PriorityQueue<interest>();
        int[][] distances = new int[N][N];  // Holds current tentative distances of all creatures
        for(int i = 0; i < N; i++)
            Arrays.fill(distances[i], Integer.MAX_VALUE);           // Which at the start is inf
        for(int i = 0; i < N; i++)
            distances[i][0] = point[i][0];                                   // Except for the start

        for(int i = 0; i < N; i++)
            queue.add(new interest(i, distances[i][0]));
        while(queue.size() > 0)
        {
            interest curr = queue.poll();       // Point closest to the visited sub-graph
            System.out.printf("%d %d %d\n", curr.id/N, curr.id%N, curr.dist);
            if(curr.id % N == N-1)    // Got home. Let's get out of here, babe
            {
                System.out.printf("%d\n", curr.dist); // That's right, I like C
                return;
            }

            int k = curr.id/N;
            int l = curr.id % N;

            int m = k-1, n = l;
            System.out.printf("Possible: %d %d\n", m,n);
            if(m >= 0 && m < N && n >= 0 && n < N && distances[m][n] != Integer.MAX_VALUE && distances[m][n] > curr.dist+point[m][n])
            {
                queue.remove(new interest(m*N+n, distances[m][n]));
                distances[m][n] = curr.dist+point[m][n];
                queue.add(new interest(m*N+n, distances[m][n]));
            }
            else if(m >= 0 && m < N && n >= 0 && n < N && distances[m][n] == Integer.MAX_VALUE)
            {
                distances[m][n] = curr.dist+point[m][n];
                queue.add(new interest(m*N+n, distances[m][n]));
            }

            m = k+1;
            n = l;
            System.out.printf("Possible: %d %d\n", m,n);
            if(m >= 0 && m < N && n >= 0 && n < N && distances[m][n] != Integer.MAX_VALUE && distances[m][n] > curr.dist+point[m][n])
            {
                queue.remove(new interest(m*N+n, distances[m][n]));
                distances[m][n] = curr.dist+point[m][n];
                queue.add(new interest(m*N+n, distances[m][n]));
            }
            else if(m >= 0 && m < N && n >= 0 && n < N && distances[m][n] == Integer.MAX_VALUE)
            {
                distances[m][n] = curr.dist+point[m][n];
                queue.add(new interest(m*N+n, distances[m][n]));
            }

            m = k;
            n = l+1;
            System.out.printf("Possible: %d %d\n", m,n);
            if(m >= 0 && m < N && n >= 0 && n < N && distances[m][n] != Integer.MAX_VALUE && distances[m][n] > curr.dist+point[m][n])
            {
                queue.remove(new interest(m*N+n, distances[m][n]));
                distances[m][n] = curr.dist+point[m][n];
                queue.add(new interest(m*N+n, distances[m][n]));
            }
            else if(m >= 0 && m < N && n >= 0 && n < N && distances[m][n] == Integer.MAX_VALUE)
            {
                distances[m][n] = curr.dist+point[m][n];
                queue.add(new interest(m*N+n, distances[m][n]));
            }

        }
    }
} 
