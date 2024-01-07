#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: 1st node of the singly linked list
 * Return: 1 if its a palindrome, 0 if not.
*/
int is_palindrome(listint_t **head)
{
	listint_t *current;
	char *str1, temp[120];
	int i, len, flag;

	if (*head == NULL)
		return (1);
	str1 = malloc(sizeof(char) * 120);
	if (str1 == NULL)
	{
		free(str1);
		return (0);
	}
	str1[0] = '\0';
	current = *head;
	while (current != NULL)
	{
		snprintf(temp, sizeof(temp), "%d", current->n);
		strcat(str1, temp);
		current = current -> next;
	}
	len = strlen(str1);
	flag = 1;
    for (i = 0; i < len / 2; i++)
    {
        if (str1[i] != str1[len - i - 1])
        {
            flag = 0;
            break;
        }
    }
    free(str1);
    return (flag);
}

