#include "lists.h"

/**
 * check_cycle - Chekcs if a linked_list has a cycle
 * @list: Linked_list to check.
 *
 * Return: 1 if there is a cycle, 0 if there'snt
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
