#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <alloca.h>

void vulnerable(char *arg)
{
	char buf[1024];
	strcpy(buf, arg);
}

int _main(int argc, char *argv[])
{
	if (argc != 2) {
		fprintf(stderr, "Error: Need a command-line argument\n");
		return 1;
	}

	FILE *f = fopen("/dev/urandom", "rb");
	assert(f);
	unsigned int r;
	fread(&r, sizeof(r), 1, f);
	fclose(f);

	alloca(r & 0xFF);

	vulnerable(argv[1]);

	return 0;
}
