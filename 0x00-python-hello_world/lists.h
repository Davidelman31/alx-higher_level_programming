#ifndef ALTERNATE_LISTS_H
#define ALTERNATE_LISTS_H
#include <stdlib.h>

/**
 * struct alternate_node - singly linked list node
 * @value: integer value
 * @next_ptr: points to the next node
 *
 * Description: Definition of a singly linked list node structure
 * 
 */
typedef struct alternate_node
{
    int value;
    struct alternate_node *next_ptr;
} alternate_list_t;

size_t alternate_print_list(const alternate_list_t *head_ptr);
alternate_list_t *alternate_add_node(alternate_list_t **head_ptr, const int value);
void alternate_free_list(alternate_list_t *head_ptr);
int alternate_check_cycle(alternate_list_t *head_ptr);

#endif /* ALTERNATE_LISTS_H */

