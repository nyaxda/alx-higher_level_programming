#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: 1st node of the singly linked list
 * Return: 1 if its a palindrome, 0 if not.
*/
int is_palindrome(listint_t **head)
{
	listint_t *current;
	char *str1, *str2, temp[120], temp2;
	int i, j, len, flag;

	if (*head == NULL)
		return (1);
	str1 = malloc(sizeof(char) * 120);
	str2 = malloc(sizeof(char) * 120);
	if (str1 == NULL || str2 == NULL)
	{
		free(str1);
		free(str2);
		return (0);
	}
	current = *head;
	while (current != NULL)
	{
		snprintf(temp, sizeof(temp), "%d", current->n);
		strcat(str1, temp);
		current = current -> next;
	}
	strcpy(str2, str1);
	len = strlen(str2);
	for (i = 0, j = len - 1; i <= j; i++, j--)
	{ 
        temp2 = str2[i]; 
        str2[i] = str2[j]; 
        str2[j] = temp2; 
    } 
	if (strcmp(str1, str2) == 0)
		flag = 1;
	else
		flag = 0;
	free(str1);
	free(str2);
	return (flag);
}
