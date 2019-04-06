#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void read_elements(FILE *f, int *buf, unsigned int count)
{
	unsigned int i;
	for (i=0; i < count; i++) {
		if (fread(&buf[i], sizeof(unsigned int), 1, f) < 1) {
			break;
		}
	}
}

void read_file(char *name)
{
	FILE *f = fopen(name, "rb");
	if (!f) {
		fprintf(stderr, "Error: Cannot open file\n");
		return;
	}

	unsigned int count;
	fread(&count, sizeof(unsigned int), 1, f);

	unsigned int *buf = alloca(count * sizeof(unsigned int));
	if (!buf) {
		return;
	}

	read_elements(f, buf, count);
}

int _main(int argc, char *argv[])
{
	if (argc != 2) {
		fprintf(stderr, "Error: Need an input filename\n");
		return 1;
	}
	read_file(argv[1]);
	return 0;
}
