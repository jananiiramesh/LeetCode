/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head) {
    struct ListNode* node1 = head;
    if (head == NULL || head->next == NULL) {
        return head;
    }
    struct ListNode* node2 = head->next;
    int temp;
    while(node2 != NULL) {
        temp = node1->val;
        node1->val = node2->val;
        node2->val = temp;
        node1 = node2->next;
        if (node1 != NULL) {
            node2 = node1->next;
        } else {
            break;
        }
    }
    return head;
}
