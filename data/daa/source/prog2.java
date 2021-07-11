
/* 2a. Design a super class called Staff with details as StaffId, Name, Phone, Salary. Extend this class by writing three subclasses namely Teaching (domain, publications), Technical (skills), and Contract (period). Write a Java program to read and display at least 3 staff objects of all three categories.
*/

import java.util.Scanner;

class Staff {
	String StaffID, Name, Phone, Salary;

	Scanner input = new Scanner(System.in);

	void read() {
		System.out.println("Enter StaffID");
		StaffID = input.nextLine();

		System.out.println("Enter Name");
		Name = input.nextLine();

		System.out.println("Enter Phone");
		Phone = input.nextLine();

		System.out.println("Enter Salary");
		Salary = input.nextLine();
	}

	void display() {
		System.out.printf("\n%-15s", "STAFFID: ");
		System.out.printf("%-15s \n", StaffID);
		System.out.printf("%-15s", "NAME: ");
		System.out.printf("%-15s \n", Name);
		System.out.printf("%-15s", "PHONE:");
		System.out.printf("%-15s \n", Phone);
		System.out.printf("%-15s", "SALARY:");
		System.out.printf("%-15s \n", Salary);
	}
}


class Teaching extends Staff {
	String Domain, Publication;

	void read_Teaching() {
		super.read(); // call super class read method
		System.out.println("Enter Domain");
		Domain = input.nextLine();
		System.out.println("Enter Publication");
		Publication = input.nextLine();
	}

	void display() {
		super.display(); // call super class display() method
		System.out.printf("%-15s", "DOMAIN:");
		System.out.printf("%-15s \n", Domain);
		System.out.printf("%-15s", "PUBLICATION:");
		System.out.printf("%-15s \n", Publication);
	}
}


class Technical extends Staff {
	String Skills;

	void read_Technical() {
		super.read(); // call super class read method
		System.out.println("Enter Skills");
		Skills = input.nextLine();
	}

	void display() {
		super.display(); // call super class display() method
		System.out.printf("%-15s", "SKILLS:");
		System.out.printf("%-15s \n", Skills);
	}
}


class Contract extends Staff {
	String Period;

	void read_Contract() {
		super.read(); // call super class read method
		System.out.println("Enter Period");
		Period = input.nextLine();
	}

	void display() {
		super.display(); // call super class display() method
		System.out.printf("%-15s", "PERIOD:");
		System.out.printf("%-15s \n", Period);
	}
}

class Staffdetails {
	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);

		System.out.println("Enter number of staff details to be created");
		int n = input.nextInt();

		Teaching steach[] = new Teaching[n];
		Technical stech[] = new Technical[n];
		Contract scon[] = new Contract[n];

		// Read Staff information under 3 categories

		for (int i = 0; i < n; i++) {
			System.out.println("Enter Teaching staff information");
			steach[i] = new Teaching();
			steach[i].read_Teaching();
		}

		for (int i = 0; i < n; i++) {
			System.out.println("Enter Technical staff information");
			stech[i] = new Technical();
			stech[i].read_Technical();
		}

		for (int i = 0; i < n; i++) {

			System.out.println("Enter Contract staff information");
			scon[i] = new Contract();
			scon[i].read_Contract();
		}

		// Display Staff Information
		System.out.println("\n STAFF DETAILS: \n");
		System.out.println("-----TEACHING STAFF DETAILS----- ");

		for (int i = 0; i < n; i++) {
			steach[i].display();
		}

		System.out.println();
		System.out.println("-----TECHNICAL STAFF DETAILS-----");
		for (int i = 0; i < n; i++) {
			stech[i].display();
		}

		System.out.println();
		System.out.println("-----CONTRACT STAFF DETAILS-----");
		for (int i = 0; i < n; i++) {
			scon[i].display();
		}

		input.close();
	}
}






/* 2b. Write a Java class called Customer to store their name and date_of_birth. The date_of_birth format should be dd/mm/yyyy. Write methods to read customer data as <name, dd/mm/yyyy> and display as <name, dd, mm, yyyy> using StringTokenizer class considering the delimiter character as �/�.
*/
import java.util.Scanner;
import java.util.StringTokenizer;

public class Customer {
	public static void main(String[] args) {
		String name;
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter Name and Date_of_Birth in the format <Name,DD/MM/YYYY>");
		name = scan.next();

		// create stringTokenizer with delimiter "/"
		StringTokenizer st = new StringTokenizer(name, ",/");

		// Count the number of tokens
		int count = st.countTokens();

		// Print one token at a time and induce new delimiter ","
		for (int i = 1; i <= count && st.hasMoreTokens(); i++) {
			System.out.print(st.nextToken());
			if (i < count)
				System.out.print(",");
		}
	}
}

