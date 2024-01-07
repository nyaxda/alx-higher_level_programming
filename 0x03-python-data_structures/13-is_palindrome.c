#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: 1st node of the singly linked list
 * Return: 1 if its a palindrome, 0 if not.
*/
int is_palindrome(listint_t **head)
{
	listint_t *fast, *slow, *pre, *curr, *next, *beg, *end;

	if (head == NULL || *head == NULL)
		return(1);
	fast = *head;
	slow = *head;
	/*moving slow to middle and fast to the end*/
	while (fast != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	pre = NULL;
	curr = slow;
	next = NULL;
	/*reversing the pointer from the middle to the end*/
	while (curr != NULL)
	{
		next = curr->next;
		curr->next = pre;
		pre = curr;
		curr = next;
	}
	/*beginning comparison*/
	beg = *head;
	end = pre;

	while (end != NULL)
	{
		if (beg->n != end->n)
			return(0);
		beg = beg->next;
		end = end->next;
	}
	return (1);
}
