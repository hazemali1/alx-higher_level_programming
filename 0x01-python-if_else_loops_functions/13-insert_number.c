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
	listint_t *s, *e;

	if (head == NULL)
		return (NULL);
	s = malloc(sizeof(listint_t));
	if (s == NULL)
		return (NULL);
	s->n = number;
	s->next = NULL;
	if (*head == NULL || (*head)->n > number)
	{
		s->next = *head;
		*head = s;
		return (s);
	}
	e = *head;
	while (e->next != NULL && e->next->n < number)
		e = e->next;
	s->next = e->next;
	e->next = s;
	return (s);
}
