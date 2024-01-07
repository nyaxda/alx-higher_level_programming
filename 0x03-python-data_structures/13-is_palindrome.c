#include lists.h

int is_palindrome(listint_t **head)
{
	listint_t *current;
	char *str1, *str2, temp;
	int i, len;

	if (*head == NULL)
		return (1);

	current = *head;
	str1 = malloc(sizeof(char) * 120);
	str2 = malloc(sizeof(char) * 120);
	while (current != NULL)
	{
		strcat(str1, (char *)current -> n);
		current = current -> next;
	}

	strcpy(str2, str1);
	len = strlen(str2);
	for (i = 0; i < len / 2; i++)
	{
		temp = str2[i];
		str2[i] = str2[len - i - 1];
		str2[len - i - 1] = temp;
	}
	if (strcmp(str1, str2) == 0)
		free(str1);
		free(str2);
		return (1);
	else
		free(str1);
		free(str2);
		return (0);
}
