#include "lists.h"

/**
 * is_palindrome - Checks if single linked list
 * is palindrome
 * @head: Address of linked list
 * Return: 0 (False) 1 (True)
 */

int is_palindrome(listint_t **head)
{
	if (!(*head))
		return (1);

	listint_t *s = *head;
	listint_t *f = *head;

	while (!s && !f)
	{
		s = s->next;
		f = f->next->next;
	}


	return (0);
}
