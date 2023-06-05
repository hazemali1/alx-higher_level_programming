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
	d = list;
	d = d->next;
	while (d != NULL)
	{
		if (d == d->next)
		{
			return (1);
		}
		s = head;
		while (s != d)
		{
			if (s == d->next)
			{
				return (1);
			}
			s = s->next;
		}
		d = d->next;
	}
	return (0);
}
