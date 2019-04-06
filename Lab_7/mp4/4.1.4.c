#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void practice(unsigned int app, unsigned int *sec, char mp[])
{
	if( strcmp(mp,"coolfood") != 0 )
	{
		printf("you think this mp is %s?\n",mp);
		return;
	}
	if( *sec != 0xc105ed)
	{
		printf("wait, sec is not closed yet\n");
		return;
	}
	if( app != 0xacce55ed)
	{
		printf("app hasn't been accessed\n");
		return;
	}
	

	printf("Good job!\n");

	return;
}

int _main()
{
	your_asm_fn();

	exit(0);
}
