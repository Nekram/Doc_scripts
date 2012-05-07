/*****************************************
*
*procMod.c 
*Short for process modulator
*This randomly changes the number of processes
* running in a given system randomly
*This will allow me to determine if VIX 
*can reassemble a task list without pausing. 
*
*
*(c) brandon marken (brandon.marken@gmail.com) 
*5-2-2012 
* 
**************************************/
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/time.h>
#include <sys/wait.h>
#define COUNT 6						//2^5 processes processes is probably good right? 
int main()
{
	pid_t procs[COUNT];
	int i;
	int status;
	//note we want this to go indefinitely however we do not want a fork bomb
	while(1)
	{
		for(i=0; i<COUNT; ++i)
		{
			procs[i]=fork();
			
		}
		for(i=0; i<COUNT;++i)
		{
		  if (procs[i]>=0)      //fork succeeded
      {
        if(procs[i]==0)
        {
          sleep(1);     //wait a sec
          exit(0);
        }
        else
        {
          wait(&status);
        }

			}
		}
	}
}
