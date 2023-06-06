#include "lists.h"

/**
 * insert_node - Insert at index
 *
 * @head: Parameter1
 * @number: Parameter2
 *
 * Return: Pointer
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *s, *e, *w, *h;

	if (head == NULL)
		return (NULL);
	s = malloc(sizeof(listint_t));
	if (s == NULL)
		return (NULL);
	h = *head;
	if (h->n > number)
	{
		s->n = number;
		s->next = *head;
		*head = s;
		return (s);
	}
	e = *head;
	e = e->next;
	w = *head;
	s->n = number;
	while (e->n < number && e != NULL)
	{
		w = w->next;
		e = e->next;
	}
	w->next = s;
	s->next = e;
	return (s);
}
