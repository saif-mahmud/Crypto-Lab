#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void print_bad_grade(void)
{
	puts("Your grade is nil.");
	exit(0);
}

void print_good_grade(void)
{
	puts("Your grade is perfect.");
	exit(1);
}

void vulnerable()
{
	char input[4];
	gets(input);
}

int _main()
{
	vulnerable();
	print_bad_grade();
	return 0;
}
