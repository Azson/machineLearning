# include <cstdio>
# include <vector>
# include <algorithm>
# include <map>

using namespace std;

/*
 * @lc app=leetcode.cn id=18 lang=cpp
 *
 * [18] 四数之和
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int> > ans;
        sort(nums.begin(), nums.end());
        int n = nums.size();
        for (int a = 0, c, d, t;a < n-3;a++) {
            if (a > 0 && nums[a] == nums[a-1])
                continue;
            if (nums[a] + nums[a+1] + nums[a+2] + nums[a+3] > target)
                break;
            if (nums[a] + nums[n-3] + nums[n-2] + nums[n-1] < target)
                continue;
            for (int b = a+1;b < n-2;b++) {
                if (b > a+1 && nums[b] == nums[b-1])
                    continue;
                
                c = b+1;
                d = n-1;
                t = nums[a] + nums[b];
                while (c < d) {
                    while (c < d && nums[c] + t + nums[d] < target) {
                        c ++;
                    }
                    
                    //printf("%d %d %d %d\n", nums[a], nums[b], nums[c], nums[d]);
                    if (c < d && nums[c] + t + nums[d] == target) {
                        vector<int> tmp (4, 0);
                        tmp[0] = nums[a]; tmp[1] = nums[b];
                        tmp[2] = nums[c]; tmp[3] = nums[d];

                        ans.push_back(tmp);
                        while (c < d && nums[c] == nums[c+1]) c++;
                        while (c < d && nums[d] == nums[d-1]) d--;
                    }
                    d --;
                }
                
            }
        }
        return ans;
    }
};
// @lc code=end

