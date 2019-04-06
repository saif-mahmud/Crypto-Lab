// Compiled with DEP enabled.
// You may need to patch the shellcode to solve this!

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct node {
	struct node *prev;
	struct node *next;
	char data[32];
} Node;

Node *list_insert(Node *after)
{
	Node *node = calloc(1, sizeof(struct node));
	if (after) {
		node->prev = after;
		if (after->next) {
			node->next = after->next;
			node->next->prev = node;
		}
		after->next = node;
	}

	return node;
}

void list_delete(Node *node)
{
	if (node->prev) {
		node->prev->next = node->next;
	}
	if (node->next) {
		node->next->prev = node->prev;
	}
}

int _main(int argc, char *argv[])
{
	if (argc != 4) {
		fprintf(stderr, "Error: Need three command-line arguments\n");
		return 1;
	}

	Node *a = list_insert(0);
	Node *b = list_insert(a);
	Node *c = list_insert(b);

	strcpy(a->data, argv[1]);
	strcpy(b->data, argv[2]);
	strcpy(c->data, argv[3]);

	list_delete(c);
	list_delete(b);
	list_delete(a);

	return 0;
}
