/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isEqual(TreeNode* left, TreeNode* right) {
        if (!left && !right)
            return true;
        if (!left || !right)
            return false;
        if (left->val != right->val) 
            return false;
        return isEqual(left->left, right->right) && isEqual(left->right, right->left);
    }
    bool isSymmetric(TreeNode* root) {
        if (!root)
            return true;
        return isEqual(root->left, root->right);
    }
};