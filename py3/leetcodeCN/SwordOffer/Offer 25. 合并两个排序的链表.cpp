/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* now = new ListNode(-1), *head;
        head = now;
        while (l1 && l2) {
            if (l1->val < l2->val) {
                now->next = l1;
                l1 = l1->next;
            }
            else {
                now->next = l2;
                l2 = l2->next;
            }
            now = now->next;
        }
        if (l1 == NULL) {
            now->next = l2;
        }
        else if (l2 == NULL) {
            now->next = l1;
        }
        return head->next;
    }
};