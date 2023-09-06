#include "lists.h"

/**
 * insert_node - Inserts a number in sorted single
 * linked list.
 * @head: Address of the first node
 * @number: number to insert
 * Return: The address of new linked list
 * otherwise NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newPtr;
	listint_t *current = *head;

	newPtr = malloc(sizeof(listint_t));
	if (newPtr == NULL)
	{
		free(newPtr);
		return (NULL);
	}

	newPtr->n = number;
	newPtr->next = NULL;

	if (*head == NULL)
	{
		newPtr->next = NULL;
		*head = newPtr;
		return (newPtr);
	}

	while (current->next != NULL && current->next->n < number)
		current = current->next;

	newPtr->next = current->next;
	current->next = newPtr;

	return (newPtr);
}
