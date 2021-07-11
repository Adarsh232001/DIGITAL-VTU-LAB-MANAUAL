/*
12. Develop a program to find the square root of a given number N and execute for all possible
inputs with appropriate messages. Note: Don’t use library function sqrt(n).
*/
#include<stdio.h>
#include<math.h>

int main()
{
  float n,result;
  printf("enter the value of n\n");
  scanf("%f",&n);
  result=pow(n,0.5);
  printf("square root of %f is %f\n",n,result);
}
