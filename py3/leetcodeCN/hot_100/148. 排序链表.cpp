# include <cstdio>
# include <stack>
# include <vector>
# include <algorithm>
# include <queue>
# include <cstring>

using namespace std;


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */



/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
 class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if (!head || head->next == NULL) {
            return head;
        }
        ListNode* slow, *fast;
        // find mid
        slow = head;
        fast = head->next;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* left, *right;
        // cut
        right = slow->next;
        slow->next = NULL;

        left = sortList(head);
        right = sortList(right);
        ListNode* p = new ListNode(0);
        ListNode* ret = p;
        while (left && right) {
            if (left->val <= right->val) {
                p->next = left;
                left = left->next;
            } else {
                p->next = right;
                right = right->next;
            }
            p = p->next;
        }
        if (left) {
            p->next = left;
        } else if (right) {
            p->next = right;
        }
        return ret->next;
    }
};



class Solution {
public:
    ListNode* sortList(ListNode* head) {
        vector<int> vec;
        ListNode* now = head;
        while (now) {
            vec.push_back(now->val);
            now = now->next;
        }
        sort(vec.begin(), vec.end());
        now = head;
        for (int & x : vec) {
            now->val = x;
            now = now->next;
        }
        return head;
    }
};


int main() {

    return 0;
}