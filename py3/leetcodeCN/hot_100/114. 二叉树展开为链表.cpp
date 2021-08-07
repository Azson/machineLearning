# include <cstdio>
# include <stack>
# include <vector>
# include <algorithm>
# include <queue>
# include <cstring>

using namespace std;


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* dfs(TreeNode* now) {
        if (now == NULL) {
            return NULL;
        }
        
        TreeNode* last_left = dfs(now->left);

        TreeNode* last_right = dfs(now->right);
        TreeNode* right = now->right;
        now->right = now->left;
        now->left = NULL;
        if (last_left)
            last_left->right = right;
        else 
            now->right = right;
        if (last_right) 
            return last_right;
        if (last_left)
            return last_left;
        return now;
    }
    void flatten(TreeNode* root) {
        dfs(root);
        
    }
};


int main() {

    return 0;
}