/* Author: Davidelman31 */

#include "lists.h"

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the initial node of the list to be reversed.
 *
 * Returns: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
    listint_t *current = *head, *next_node, *previous = NULL;

    while (current)
    {
        next_node = current->next;
        current->next = previous;
        previous = current;
        current = next_node;
    }

    *head = previous;
    return *head;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Returns: 0 if the linked list is not a palindrome, 1 if it is.
 */
int is_palindrome(listint_t **head)
{
    listint_t *temp, *reversed, *middle;
    size_t size = 0, i;

    if (*head == NULL || (*head)->next == NULL)
        return 1;

    temp = *head;
    while (temp)
    {
        size++;
        temp = temp->next;
    }

    temp = *head;
    for (i = 0; i < (size / 2) - 1; i++)
        temp = temp->next;

    if ((size % 2) == 0 && temp->n != temp->next->n)
        return 0;

    temp = temp->next->next;
    reversed = reverse_listint(&temp);
    middle = reversed;

    temp = *head;
    while (reversed)
    {
        if (temp->n != reversed->n)
            return 0;
        temp = temp->next;
        reversed = reversed->next;
    }
    reverse_listint(&middle);

    return 1;
}

