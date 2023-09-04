#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Checks single linked list for cycles
 * @list: Link list
 * @Return: 0 (False), 1 (True)
 */

int check_cycle(listint_t *list)
{
	listint_t *check = list;
	listint_t *match = list;


	while (check != match)
	{
		if (!match || !match->next)
			return (0);
		check = check->next;
		match = match->next->next;
	}
	return (1);
}
