/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* createNode(int data){
    struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
    newNode->val=data;
    newNode->next=NULL;
    return newNode;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *head = NULL, *newNode, *traverse = NULL;
    int sum;
    bool carry = false;

    while (l1 != NULL || l2 != NULL) {
        sum = (l1 ? l1->val : 0) + (l2 ? l2->val : 0);
        
        if (carry) {
            sum++;
            carry = false;
        }
        if (sum >= 10) {
            carry = true;
            sum = sum % 10;
        }
        
        newNode = createNode(sum);
        if (head == NULL) {
            head = newNode;
            traverse = head;
        } else {
            traverse->next = newNode;
            traverse = traverse->next;
        }
        
        if (l1) l1 = l1->next;
        if (l2) l2 = l2->next;
    }

    // Handle the final carry, if any
    if (carry) {
        newNode = createNode(1);
        traverse->next = newNode;
    }
    
    return head;
}
