/* 8. Kruskals */

import java.util.Scanner;

public class KruskalsClass {

	final static int MAX = 20;
	static int n; // No. of vertices of G
	static int cost[][]; // Cost matrix
	static Scanner scan = new Scanner(System.in);

	public static void main(String[] args) {
		ReadMatrix();
		Kruskals();
	}

	static void ReadMatrix() {

		int i, j;
		cost = new int[MAX][MAX];

		System.out.println("Implementation of Kruskal's algorithm");
		System.out.println("Enter the no. of vertices");
		n = scan.nextInt();

		System.out.println("Enter the cost adjacency matrix");
		for (i = 1; i <= n; i++) {
			for (j = 1; j <= n; j++) {
				cost[i][j] = scan.nextInt();
				if (cost[i][j] == 0)
					cost[i][j] = 999;
			}
		}
	}

	static void Kruskals() {

		int a = 0, b = 0, u = 0, v = 0, i, j, ne = 1, min, mincost = 0;

		System.out.println("The edges of Minimum Cost Spanning Tree are");
		while (ne < n) {
			for (i = 1, min = 999; i <= n; i++) {
				for (j = 1; j <= n; j++) {
					if (cost[i][j] < min) {
						min = cost[i][j];
						a = u = i;
						b = v = j;
					}
				}
			}
			u = find(u);
			v = find(v);
			if (u != v) {
				uni(u, v);
				System.out.println(ne++ + "edge (" + a + "," + b + ") =" + min);
				mincost += min;
			}
			cost[a][b] = cost[b][a] = 999;
		}
		System.out.println("Minimum cost :" + mincost);
	}

	static int find(int i) {
		int parent[] = new int[9];
		while (parent[i] == 1)
			i = parent[i];
		return i;
	}

	static void uni(int i, int j) {
		int parent[] = new int[9];
		parent[j] = i;
	}
}
