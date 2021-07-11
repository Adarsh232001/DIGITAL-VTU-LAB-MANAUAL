/*Design, Develop and Implement a Program in C for the following Stack Applications
a. Evaluation of Suffix expression with single digit operands and operators: +, -, *, /, %,^
b. Solving Tower of Hanoi problem with n disks*/

//A  Evaluation of Suffix expression with single digit operands and operators: +, -, *, /, %,^
#include<stdio.h>
#include<math.h>
#include<string.h>

float compute(char symbol, float op1, float op2)
{
	switch (symbol)
	{
		case '+': return op1 + op2;
		case '-': return op1 - op2;
		case '*': return op1 * op2;
		case '/': return op1 / op2;
		case '$':
		case '^': return pow(op1,op2);
		default : return 0;
	}
}

void main()
{
float s[20], res, op1, op2;
int top, i;
char postfix[20], symbol;
printf("\nEnter the postfix expression:\n");
scanf ("%s", postfix);
top=-1;
for (i=0; i<strlen(postfix) ;i++)
{
symbol = postfix[i];
if(isdigit(symbol))
	s[++top]=symbol - '0';
else
	{
	op2 = s[top--];
	op1 = s[top--];
	res = compute(symbol, op1, op2);
	s[++top] = res;
	}
}
res = s[top--];
printf("\nThe result is : %f\n", res);
}

//B   Solving Tower of Hanoi problem with n disks
#include<stdio.h>
#include<math.h>
void tower(int n, int source, int temp, int destination);

void tower(int n, int source, int temp, int destination)
{
if(n == 0)
	return;
tower(n-1, source, destination, temp);
printf("\nMove disc %d from %c to %c", n, source, destination);
tower(n-1, temp, source, destination);
}

void main ()
{
int n;
printf("\nEnter the number of discs: \n\n");
scanf("%d", &n);
printf("\nThe sequence of moves involved in the Tower of Hanoi are\n");
tower(n, 'A', 'B', 'C');
printf("\n\nTotal Number of moves are: %d\n", (int)pow(2,n)-1);
}