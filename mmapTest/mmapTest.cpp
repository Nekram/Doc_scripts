#include <sys/types.h>
#include <sys/mman.h>
#include <iostream>
#include <cstdlib>
#include <chrono>
#include <cstring>
#include <thread>
#include <array>
#include <vector>
#define PAGE_SIZE 4096
#define SIZE 4*PAGE_SIZE 

using namespace std;


int main()
{

	void  * ptr;
	unsigned char * other;
	int k;
	const int theSize=10000000;
	vector<double> data(theSize);
 std::chrono::time_point<std::chrono::high_resolution_clock> start, end;
	

for(int k=0; k<theSize; ++k)
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
	
	data[k]=chrono::duration_cast<chrono::nanoseconds>(dt).count();
//	this_thread::sleep_for(chrono::milliseconds(1));
	}	
	
	for(double i : data)
	{
		cout << i << endl;
	}
	return 0;
}

