/* Program 5
Sort a given set of n integer elements using Merge Sort method and compute its time complexity. Run the program for varied values of n > 5000, and record the time taken to sort. Plot a graph of the time taken versus n on graph sheet. The elements can be read from a file or can be generated using the random number generator. Demonstrate using Java how the divide-and-conquer method works along with its time complexity analysis: worst case, average case and best case.
*/
import java.util.Random;
import java.util.Scanner;

public class MergeSort2 {
	static final int MAX = 10005;
	static int[] a = new int[MAX];

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("Enter Max array size: ");
		int n = input.nextInt();
		Random random = new Random();
		System.out.println("Enter the array elements: ");
		for (int i = 0; i < n; i++)
		//	a[i] = input.nextInt(); // for keyboard entry
		 a[i] = random.nextInt(1000); // generate random numbers �
// uniform distribution
		long startTime = System.nanoTime();
		MergeSortAlgorithm(0, n - 1);
		long stopTime = System.nanoTime();
		long elapsedTime = stopTime - startTime;
		System.out.println("Time Complexity (ms) for n = " +
n + " is : " + (double) elapsedTime / 1000000);
		System.out.println("Sorted Array (Merge Sort):");
		for (int i = 0; i < n; i++)
			System.out.print(a[i] + " ");
		input.close();
	}

	public static void MergeSortAlgorithm(int low, int high) {
		int mid;
		if (low < high) {
			mid = (low + high) / 2;
			MergeSortAlgorithm(low, mid);
			MergeSortAlgorithm(mid + 1, high);
			Merge(low, mid, high);
		}
	}

	public static void Merge(int low, int mid, int high) {
		int[] b = new int[MAX];
		int i, h, j, k;
		h = i = low;
		j = mid + 1;
		while ((h <= mid) && (j <= high))
			if (a[h] < a[j])
				b[i++] = a[h++];
			else
				b[i++] = a[j++];

		if (h > mid)
			for (k = j; k <= high; k++)
				b[i++] = a[k];
		else
			for (k = h; k <= mid; k++)
				b[i++] = a[k];

		for (k = low; k <= high; k++)
			a[k] = b[k];
	}
}
