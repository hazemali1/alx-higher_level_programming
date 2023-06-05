#include "lists.h"

/**
 * find_listint_loop - Finding
 *
 * @list: Parameter
 *
 * Return: 0 or 1
*/
int check_cycle(listint_t *list)
{
	listint_t *s, *d;

	if (list == NULL)
	{
		return (0);
	}
	s = list;
	d = list->next;
	while (d != NULL && d->next != NULL)
	{
		if (d == s || d->next == s)
			return (1);
		s = s->next;
		d = d->next->next;
	}
	return (0);
}
