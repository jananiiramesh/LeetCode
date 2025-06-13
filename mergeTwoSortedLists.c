/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    if (list1 == NULL) return list2;
    if (list2 == NULL) return list1;

    struct ListNode* t1 = list1;
    struct ListNode* t2 = list2;
    struct ListNode* t1_prev = NULL;

    if (t2->val < t1->val) {
        list1 = t2;
        t2 = t2->next;
        list1->next = t1;
        t1_prev = list1;
        t1 = t1_prev->next;
    }

    while (t1 != NULL && t2 != NULL) {
        if (t1->val <= t2->val) {
            t1_prev = t1;
            t1 = t1->next;
        } else {
            struct ListNode* temp = t2->next;
            t1_prev->next = t2;
            t2->next = t1;
            t1_prev = t2;
            t2 = temp;
        }
    }

    if (t2 != NULL) {
        t1_prev->next = t2;
    }

    return list1;
}
