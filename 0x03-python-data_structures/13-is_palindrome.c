#include "lists.h"

/**
 * is_palindrome - Check
 *
 * @head: Parameter
 *
 * Return: 0, 1
*/
int is_palindrome(listint_t **head)
{
	listint_t *s, *d, *f;
	int w = 0, q, l[1024];

	s = *head;
	while (s != NULL)
	{
		w++;
		s = s->next;
	}
	if (w % 2 == 0)
		w = w / 2;
	else
		w = w / 2 + 1;
	d = *head;
	while (w > 0)
	{
		d = d->next;
		w--;
	}
	for (q = 0; d != NULL; q++)
	{
		l[q] = d->n;
		d = d->next;
	}
	f = *head;
	q--;
	while (q >= 0)
	{
		if (f->n != l[q])
			return (0);
		f = f->next;
		q--;
	}
	return (1);
}
