#include <stdlib.h>
#include <time.h>
#include <stdio.h>


int main()
{

	clock_t c0, c1; // our clocks
	int i,j,k;			// counters


	//going for a standard test size of 2000 iterations unless otherwise
	//necessary
	for(i=0; i<2000; ++i)
	{
		c0 = clock();
		for (j=0;j<100000000; ++j)
			asm("movl $1,%eax");
		
		c1 = clock();

		printf("%f\n",((double)(c1-c0))/CLOCKS_PER_SEC);
	}
	
	return 0;
}
