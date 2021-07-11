
/* 3a. Write a Java program to read two integers a and b. Compute a/b and print, when b is not zero. Raise an exception when b is equal to zero.
*/
import java.util.Scanner;

class exception {

	public static void main(String[] args) {
		int a, b, result;

		Scanner input = new Scanner(System.in);
		System.out.println("Input two integers");

		a = input.nextInt();
		b = input.nextInt();

		try {
			result = a / b;
			System.out.println("Result = " + result);
		}

		catch (ArithmeticException e) {
			System.out.println("Exception caught: Division by zero.");
		}
	}
}






/* 3b. Write a Java program that implements a multi-thread application that has three threads. First thread generates a random integer for every 1 second; second thread computes the square of the number and prints; third thread will print the value of cube of the number.
*/
import java.util.Random;

class SquareThread implements Runnable {
	int x;

	SquareThread(int x) {
		this.x = x;
	}

	public void run() {
		System.out.println("Thread Name:Square Thread and Square of " + x + " is: " + x * x);
	}
}

class CubeThread implements Runnable {
	int x;

	CubeThread(int x) {
		this.x = x;
	}

	public void run() {
		System.out.println("Thread Name:Cube Thread and Cube of " + x + " is: " + x * x * x);
	}
}

class RandomThread implements Runnable {
	Random r;
	Thread t2, t3;

	public void run() {
		int num;
		r = new Random();
		try {

			while (true) {
				num = r.nextInt(100);
				System.out.println("Main Thread and Generated Number is " + num);
				t2 = new Thread(new SquareThread(num));
				t2.start();

				t3 = new Thread(new CubeThread(num));
				t3.start();

				Thread.sleep(1000);
				System.out.println("--------------------------------------");
			}
		} catch (Exception ex) {
			System.out.println("Interrupted Exception");
		}
	}
}

public class MainThread {
	public static void main(String[] args) {

		RandomThread thread_obj = new RandomThread();
		Thread t1 = new Thread(thread_obj);
		t1.start();
	}
}
