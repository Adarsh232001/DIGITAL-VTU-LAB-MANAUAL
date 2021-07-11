/* 10a. Floyd's */

import java.util.Scanner;
public class FloydsClass {
	static final int MAX = 20; 	// max. size of cost matrix
	static int a[][];			// cost matrix
	static int n; 				// actual matrix size

	public static void main(String args[]) {
		a = new int[MAX][MAX];
		ReadMatrix();
		Floyds();				// find all pairs shortest path
		PrintMatrix();
	}

	static void ReadMatrix() {
		System.out.println("Enter the number of vertices\n");
		Scanner scanner = new Scanner(System.in);
		n = scanner.nextInt();
		System.out.println("Enter the Cost Matrix (999 for infinity) \n");
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				a[i][j] = scanner.nextInt();
			}
		}
		scanner.close();
	}

	static void Floyds() {
		for (int k = 1; k <= n; k++) {
			for (int i = 1; i <= n; i++)
				for (int j = 1; j <= n; j++)
					if ((a[i][k] + a[k][j]) < a[i][j])
						a[i][j] = a[i][k] + a[k][j];
		}
	}

	static void PrintMatrix() {
		System.out.println("The All Pair Shortest Path Matrix is:\n");
		for(int i=1; i<=n; i++)
		{
			for(int j=1; j<=n; j++)
				System.out.print(a[i][j] + "\t");
			System.out.println("\n");
		}
	}
}




/* 10b. TSP - DP */

import java.util.Scanner;

public class TravSalesPerson {
	static int MAX = 100;
	static final int infinity = 999;

	public static void main(String args[]) {
 		int cost = infinity;
		int c[][] = new int[MAX][MAX]; 	// cost matrix
		int tour[] = new int[MAX]; 		// optimal tour
		int n; 							// max. cities
		System.out.println("Travelling Salesman Problem using Dynamic Programming\n");
		System.out.println("Enter number of cities: ");
		Scanner scanner = new Scanner(System.in);
		n = scanner.nextInt();
		System.out.println("Enter Cost matrix:\n");
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++) {
				c[i][j] = scanner.nextInt();
				if (c[i][j] == 0)
					c[i][j] = 999;
			}
		for (int i = 0; i < n; i++)
			tour[i] = i;
		cost = tspdp(c, tour, 0, n);
		// print tour cost and tour
		System.out.println("Minimum Tour Cost: " + cost);
		System.out.println("\nTour:");
		for (int i = 0; i < n; i++) {
			System.out.print(tour[i] + " -> ");
		}
		System.out.println(tour[0] + "\n");
		scanner.close();
	}

	static int tspdp(int c[][], int tour[], int start, int n) {
		int i, j, k;
		int temp[] = new int[MAX];
		int mintour[] = new int[MAX];
		int mincost;
		int cost;
		if (start == n - 2)
			return c[tour[n - 2]][tour[n - 1]] + c[tour[n - 1]][0];
		mincost = infinity;
		for (i = start + 1; i < n; i++) {
			for (j = 0; j < n; j++)
				temp[j] = tour[j];
			temp[start + 1] = tour[i];
			temp[i] = tour[start + 1];
			if (c[tour[start]][tour[i]] + (cost = tspdp(c, temp, start + 1, n)) < mincost) {
				mincost = c[tour[start]][tour[i]] + cost;
				for (k = 0; k < n; k++)
					mintour[k] = temp[k];
			}
		}
		for (i = 0; i < n; i++)
			tour[i] = mintour[i];
		return mincost;
	}
}
