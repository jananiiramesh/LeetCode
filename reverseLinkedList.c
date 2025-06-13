/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* prev = NULL;
    struct ListNode* curr = head;
    struct ListNode* next_temp = NULL;
    while (curr != NULL) {
        next_temp = curr -> next;
        curr -> next = prev;
        prev = curr;
        curr = next_temp;
    }
    head = prev;
    return head;
}
