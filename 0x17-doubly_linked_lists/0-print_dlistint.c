#include "lists.h"

/**
 * print_dlistint - prints all the elements of a dlistint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
    struct dlistint_s *current = h;
    int count = 0;

    while (current != NULL)
    {
        current = current->next;
        count++;
    }
    return count;
}