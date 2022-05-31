#include "lists.h"

/**
 * check_cycle - check if a singly linked list contains a loop
 * @list: pointer to head of a list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *f = list;
	listint_t *s = list;

	while (f && (f = f->next))
	{
		if (f == s)
			return (1);

		f = f->next;
		s = s->next;
	}
	return (0);
}
