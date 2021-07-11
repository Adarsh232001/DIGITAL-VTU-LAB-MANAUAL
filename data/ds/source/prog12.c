/*Given a File of N employee records with a set K of Keys (4-digit) which uniquely determine
the records in file F. Assume that file F is maintained in memory by a Hash Table (HT) of m
memory locations with L as the set of memory addresses (2-digit) of locations in HT. Let the
keys in K and addresses in L are Integers. Design and develop a Program in C that uses Hash
function H: K ®L as H(K)=K mod m (remainder method), and implement hashing
technique to map a given key K to the address space L. Resolve the collision (if any) using
linear probing.*/

#include <stdio.h>
#include <stdlib.h>
#define MAX 5
#define mod(x) x%MAX
void linear_prob(int a[],int num,int key)
{
    if(a[key]==-1)
        a[key]=num;
    else
    {
        printf("\nCollision detected!!");
        int i;
        for(i=mod(key+1);i!=key;i=mod(++i))
            if(a[i]==-1)
            break;
        if(i!=key)
        {
            printf("\nCollision avoided successfully\n");
            a[i]=num;
        }
        else
            printf("\nHash table is full\n");
    }
}
void display(int a[])
{
    short ch,i;
    printf("\n1.Filtered display\n2.Display all\nEnter choice:");
    scanf("%d",&ch);
    printf("\nHash table is :\n");
    for(i=0;i<MAX;i++)
        if(a[i]>0||ch-1)
            printf("%d  %d\n",i,a[i]);
}
int main()
{
    int a[MAX],num,i;
    printf("\nCollision handling by linear probing");
    for(i=0;i<MAX;a[i++]=-1);
    do
    {
        printf("\nEnter the data:");
        scanf("%4d",&num);
        linear_prob(a,num,mod(num));
        printf("Do u wish to continue(1/0):");
        scanf("%d",&i);
    }while(i);
    display(a);
    return 0;
}