#include <sys/types.h>
#include <sys/mman.h>
#include <iostream>
#include <cstdlib>
#include <chrono>
#include <cstring>
#define PAGE_SIZE 4096
#define SIZE 4*PAGE_SIZE 

using namespace std;


int main()
{

	void  * ptr;
	unsigned char * other;
	int k;
 std::chrono::time_point<std::chrono::high_resolution_clock> start, end;
	

for(int k=0; k<100; ++k)
{
	 start = std::chrono::high_resolution_clock::now();
		int i;
		for(  i=0; i<1; ++i)
		{
			ptr = mmap((void*)0, SIZE, PROT_READ+PROT_WRITE,MAP_ANONYMOUS+MAP_SHARED,-1,0);
			munmap(ptr,SIZE);
		}
end = std::chrono::high_resolution_clock::now();
	chrono::duration<double> dt=end-start;
	
	cout << chrono::duration_cast<chrono::nanoseconds>(dt).count() << endl;
	
	}	
	return 0;
}
