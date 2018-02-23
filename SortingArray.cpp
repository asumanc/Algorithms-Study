/*This program gives ascending and 
descending order of an array elements*/

#include <stdio.h>

int main(void)
{
	int a[5], i=0, j=0, n, t;
	
	scanf ("%d", &n);
	printf ("\n");

	for (i = 0; i <n; i++){
		printf ("\n%d",(i+1));
		scanf ("%d", &a[i]);
	}

	for (j=0 ; j<(n-1) ; j++){
		for (i=0 ; i<(n-1); i++){
			if (a[i+1] < a[i]){
				t=a[i];
				a[i]=a[i+1];
				a[i+1]=t;
			}
		}
	}

	printf ("Ascending order\n");
		for (i=0; i<n; i++)
	{
		printf (" %d\n", a[i]);
	}

	printf ("Descending order\n: ");
	for (i=n; i>0; i--)
	{
		printf (" %d\n", a[i-1]);
	}
	


      
      return 0;
}

