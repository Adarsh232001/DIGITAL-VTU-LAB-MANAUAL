/*Program 4.
Sort a given set of n integer elements using Quick Sort method and compute its time complexity. Run the program for varied values of n > 5000 and record the time taken to sort. Plot a graph of the time taken versus n on graph sheet. The elements can be read from a file or can be generated using the random number generator. Demonstrate using Java how the divide-and-conquer method works along with its time complexity analysis: worst case, average case and best case.
*/
import java.util.Scanner;
import java.util.Arrays;
import java.util.Random;

public class QuickSortComplexity {
	static final int MAX = 10005;
	static int[] a = new int[MAX];
	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		System.out.print("Enter Max array size: ");
		int n = input.nextInt();
		Random random = new Random();
		System.out.println("Enter the array elements: ");
		for (int i = 0; i < n; i++)
			 a[i] = input.nextInt();   // for keyboard entry
	// a[i] = random.nextInt(1000); // generate
      // random numbers � uniform distribution

		// a = Arrays.copyOf(a, n); // keep only non zero elements
		// Arrays.sort(a); // for worst-case time complexity

		System.out.println("Input Array:");
		for (int i = 0; i < n; i++)
			System.out.print(a[i] + " ");
		// set start time
		long startTime = System.nanoTime();
		QuickSortAlgorithm(0, n - 1);
		long stopTime = System.nanoTime();
		long elapsedTime = stopTime - startTime;
		System.out.println("\nSorted Array:");
		for (int i = 0; i < n; i++)
			System.out.print(a[i] + " ");
		System.out.println();
		System.out.println("Time Complexity in ms for
                     n=" + n + " is: " + (double) elapsedTime / 1000000);
	}

	public static void QuickSortAlgorithm(int p, int r) {
		int i, j, temp, pivot;
		if (p < r) {
			i = p;
			j = r + 1;
			pivot = a[p]; // mark first element as pivot
			while (true) {
				i++;
				while (a[i] < pivot && i < r)
					i++;
				j--;
				while (a[j] > pivot)
					j--;
				if (i < j) {
					temp = a[i];
					a[i] = a[j];
					a[j] = temp;
				} else
					break; // partition is over
			}
			a[p] = a[j];
			a[j] = pivot;
			QuickSortAlgorithm(p, j - 1);
			QuickSortAlgorithm(j + 1, r);
		}
	}
}
