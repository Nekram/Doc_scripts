#include <sys/types.h>
#include <iostream>
#include <cstdlib>
#include <chrono>
#include <cstring>
#define PAGE_SIZE 4096
#define SIZE 2*PAGE_SIZE 

using namespace std;


int main()
{

	unsigned char * ptr;
	unsigned char * other;
	int k;
 std::chrono::time_point<std::chrono::system_clock> start, end;
	

//for(int k=0; k<100; ++k)
{
	 start = std::chrono::system_clock::now();
		int i;
		for(  i=0; i<1; ++i)
		{
			ptr=new unsigned char[SIZE];
			delete[] ptr;
		}
end = std::chrono::system_clock::now();
	chrono::duration<double> dt=end-start;
	
	cout << chrono::duration_cast<chrono::microseconds>(dt).count() << endl;
	
	}	
	return 0;
}
