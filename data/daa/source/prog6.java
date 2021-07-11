/* Knapsack DP */

import java.util.Scanner;

public class KnapsackDP {
	static final int MAX = 20; // max. no. of objects
	static int w[]; 	// weights 0 to n-1
	static int p[]; 	// profits 0 to n-1
	static int n; 		// no. of objects
	static int M; 		// capacity of Knapsack
	static int V[][]; 	// DP solution process - table
	static int Keep[][]; // to get objects in optimal solution

	public static void main(String args[]) {
		w = new int[MAX];
		p = new int[MAX];
		V = new int [MAX][MAX];
		Keep = new int[MAX][MAX];
		int optsoln;
		ReadObjects();
		for (int i = 0; i <= M; i++)
			V[0][i] = 0;
		for (int i = 0; i <= n; i++)
			V[i][0] = 0;
		optsoln = Knapsack();
		System.out.println("Optimal solution = " + optsoln);
	}

	static int Knapsack() {
		int r; // remaining Knapsack capacity
		for (int i = 1; i <= n; i++)
			for (int j = 0; j <= M; j++)
				if ((w[i] <= j) && (p[i] + V[i - 1][j - w[i]] > V[i - 1][j])) {
					V[i][j] = p[i] + V[i - 1][j - w[i]];
					Keep[i][j] = 1;
				} else {
					V[i][j] = V[i - 1][j];
					Keep[i][j] = 0;
				}

		// Find the objects included in the Knapsack
		r = M;
		System.out.println("Items = ");
		for (int i = n; i > 0; i--) // start from Keep[n,M]
			if (Keep[i][r] == 1) {
				System.out.println(i + " ");
				r = r - w[i];
			}
		System.out.println();
		return V[n][M];
	}

	static void ReadObjects() {
		Scanner scanner = new Scanner(System.in);
		System.out.println("Knapsack Problem - Dynamic Programming Solution: ");
		System.out.println("Enter the max capacity of knapsack: ");
		M = scanner.nextInt();
		System.out.println("Enter number of objects:  ");
		n = scanner.nextInt();
		System.out.println("Enter Weights: ");
		for (int i = 1; i <= n; i++)
			w[i] = scanner.nextInt();
		System.out.println("Enter Profits: ");
		for (int i = 1; i <= n; i++)
			p[i] = scanner.nextInt();
		scanner.close();
	}
}



/* Knapsack Greedy */

import java.util.Scanner;
class KObject {					// Knapsack object details
	float w;
	float p;
	float r;
}
public class KnapsackGreedy2 {
	static final int MAX = 20; 	// max. no. of objects
	static int n;				// no. of objects
	static float M;				// capacity of Knapsack

	public static void main(String args[]) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("Enter number of objects:  ");
		n = scanner.nextInt();
		KObject[] obj = new KObject[n];
		for(int i = 0; i<n;i++)
			obj[i] = new KObject();// allocate memory for members

		ReadObjects(obj);
		Knapsack(obj);
		scanner.close();
	}

	static void ReadObjects(KObject obj[]) {
		KObject temp = new KObject();
		Scanner scanner = new Scanner(System.in);
		System.out.println("Enter the max capacity of knapsack: ");
		M = scanner.nextFloat();

		System.out.println("Enter Weights: ");
		for (int i = 0; i < n; i++)
			obj[i].w = scanner.nextFloat();

		System.out.println("Enter Profits: ");
		for (int i = 0; i < n; i++)
			obj[i].p = scanner.nextFloat();

		for (int i = 0; i < n; i++)
			obj[i].r = obj[i].p / obj[i].w;

		// sort objects in descending order, based on p/w ratio
		for(int i = 0; i<n-1; i++)
			for(int j=0; j<n-1-i; j++)
				if(obj[j].r < obj[j+1].r){
					temp = obj[j];
					obj[j] = obj[j+1];
					obj[j+1] = temp;
				}
		scanner.close();
	}

	static void Knapsack(KObject kobj[]) {
		float x[] = new float[MAX];
		float totalprofit;
		int i;
		float U;  // U place holder for M
		U = M;
		totalprofit = 0;
		for (i = 0; i < n; i++)
			x[i] = 0;
		for (i = 0; i < n; i++) {
			if (kobj[i].w > U)
				break;
			else {
				x[i] = 1;
				totalprofit = totalprofit + kobj[i].p;
				U = U - kobj[i].w;
			}
		}
		System.out.println("i = " + i);
		if (i < n)
			x[i] = U / kobj[i].w;
		totalprofit = totalprofit + (x[i] * kobj[i].p);
		System.out.println("The Solution vector, x[]: ");
		for (i = 0; i < n; i++)
			System.out.print(x[i] + " ");
		System.out.println("\nTotal profit is = " + totalprofit);
	}
 }

