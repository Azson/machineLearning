#include <vector>

class Solution {
public:
    /**
     * 返回所求中序序列
     * @param n int整型 二叉树节点数量
     * @param pre int整型vector 前序序列
     * @param suf int整型vector 后序序列
     * @return int整型vector
     */
    vector<int> ans;
    void do_tree(int pl, int pr, vector<int>& pre, int sl, int sr, vector<int>& suf) {
        if (pl > pr) return;
        if (pl == pr) {
            ans.push_back(pre[pl]);
            return ;
        }
        int pos = -1;
        for(int i = sl;i <= sr;i ++) {
            if(pre[pl+1] == suf[i]) {
                pos = i;
                break;
            }
        }
        do_tree(pl+1, pos-sl+pl+1, pre, sl, pos-1, suf);
        ans.push_back(pre[pl]);
        do_tree(pos-sl+pl+2, pr, pre, pos+1, sr, suf);
    }
    vector<int> solve(int n, vector<int>& pre, vector<int>& suf) {
        // write code here
        do_tree(0, n-1, pre, 0, n-1, suf);
        return ans;
    }

    
};