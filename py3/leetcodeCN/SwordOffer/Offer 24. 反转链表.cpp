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
    ListNode* reverseList(ListNode* head) {
        ListNode* pre=NULL, *now=head, *next;
        if (head)
            next = head->next;
        while (now != NULL) {
            now->next = pre;
            pre = now;
            now = next;
            if (next != NULL)
                next = next->next;
        }
        return pre;
    }
};