#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
	time_t t0, t1;
	clock_t c0, c1;

	long count;
	int * ptr;
	t0=time(NULL);		//initial time	

	while(1)
	{
		int i;
		for( int i=0; i<10; ++i)
		{
			ptr=malloc(4096*sizeof(int));
			free(ptr);
		}
	}
}
