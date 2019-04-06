// Code for format string attack

#include <stdio.h>
#include <string.h>

void vulnerable(char *arg)
{
	char buf[2048];

	strncpy(buf, arg, sizeof(buf));

	printf(buf);

}

int _main(int argc, char **argv)
{
	if (argc != 2) {
		fprintf(stderr, "Error: need a command-line argument\n");
		return 1;
	}
	vulnerable(argv[1]);
	return 0;
}
