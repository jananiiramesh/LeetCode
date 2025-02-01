/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode* traverse = head;
    struct ListNode* del = traverse;
    int len=0;
    for (int i=0;i<n;i++){
        len++;
        if (len==n && traverse->next == NULL){
            //len of list equal to n, remove first node
            head = head->next;
            return head;
        }
        if (traverse->next == NULL){
            //nth node to be deleted from the end doesn't exist
            return NULL;
        }
        traverse = traverse->next;
    }
    while(traverse->next != NULL){
        traverse = traverse->next;
        del = del->next;
    }
    if (n==1){
        //delete last node
        del->next = NULL;
        return head;
    }
    del->next = del->next->next;
    return head;
}