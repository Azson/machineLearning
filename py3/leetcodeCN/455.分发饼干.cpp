/*
 * @lc app=leetcode.cn id=455 lang=cpp
 *
 * [455] 分发饼干
 */

// @lc code=start
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int n = s.size(), m = g.size();
        int ans = 0;
        for (int i = 0, j = 0;i < n;i++) {
            if (s[i] >= g[j]) {
                j ++;
                ans ++;
                if (j >= m) break;
            }
        }
        return ans;
    }
};
// @lc code=end

