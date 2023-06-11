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

	s = *head;
	d = *head;
	while (d->next != NULL)
		d = d->next;
	while (s != d)
	{
		if (s->n != d->n)
			return (0);
		f = *head;
		while (f->next != d)
			f = f->next;
		s = s->next;
		d = f;
	}
	return (1);
}
