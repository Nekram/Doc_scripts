#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define PAGE_SIZE 4096
#define SIZE 2*PAGE_SIZE 
int main()
{
	clock_t c0, c1;

	int * ptr;
	int * other;
	int k;


	{
		int i;
		c0=clock();
		for(  i=0; i<100000; ++i)
		{
			ptr=malloc(SIZE*sizeof(int));
			memset(ptr,1,SIZE);
			int j;
			other=ptr;
			for (j=0;j<SIZE; ++j)
				other++;
			free(ptr);
		}
		c1=clock();
		printf("%f\n",(double)((double)(c1-c0)/CLOCKS_PER_SEC));
	}
}
