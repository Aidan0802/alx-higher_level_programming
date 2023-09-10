#include "lists.h"

/**
 * is_palindrome - Checks if single linked list
 * is palindrome
 * @head: Address of linked list
 * Return: 0 (False) 1 (True)
 */

int is_palindrome(listint_t **head)
{
	listint_t *s = *head;
	listint_t *f = *head;
	listint_t *sec_half = NULL;
	listint_t *fir_half = NULL;

	if (!(*head))
		return (1);

	while (!s && !f)
	{
		s = s->next;
		f = f->next->next;
	}
	sec_half = rev_list(s->next);
	fir_half = *head;

	while (sec_half)
		if (sec_half->n != fir_half->n)
			return (0);

	return (1);
}

/**
 * rev_list - Reverse the list
 * @head: Address of the head to be
 * reversed
 * Return: Reversed list
 */

listint_t *rev_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;
	
	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}
