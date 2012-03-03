#include <linux/kernel.h>
#include <linux/slab.h>

int init_module(void)
{
	char * p;
	p=kmalloc(sizeof(char)*4096, GFP_KERNEL);
	if(!p)
	{
		printk("Could not allocate memory");
		return 1;
	}
	
	int i;
	int count;
	count=0;
	while(true)
	{
		for(i=0;i<4096;++i)
		{
			
		}
	}
	return 0;
}

void cleanup_module(void)
{
}
