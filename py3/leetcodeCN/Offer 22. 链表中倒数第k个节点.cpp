# include <cstdio>
# include <string>
# include <map>
# include <string>
# include <algorithm>
# include <queue>

using namespace std;

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
    ListNode* getKthFromEnd(ListNode* head, int k) {
        ListNode* left = head, *right = head;
        while (k--) {
            right = right->next;
        }
        while (right) {
            left = left->next;
            right = right->next;
        }
        return left;
    }
};