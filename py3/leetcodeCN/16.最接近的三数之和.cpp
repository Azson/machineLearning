# include <cstdio>
# include <vector>
# include <algorithm>

using namespace std;

/*
 * @lc app=leetcode.cn id=16 lang=cpp
 *
 * [16] 最接近的三数之和
 */

// @lc code=start
class Solution {
public:
    void update_ans(int& ans, int tmp, int& target) {
        if (abs(ans - target) > abs(tmp - target))
            ans = tmp;
    }
    int threeSumClosest(vector<int>& nums, int target) {
        int n = nums.size(), ans = 1e7;
        sort(nums.begin(), nums.end());
        for (int i = 0, j, k, t;i < n;i++) {
            j = i+1;
            k = n-1;
            while (j < k) {
                t = nums[i] + nums[j] + nums[k];
                if (t == target) {
                    return target;
                }
                update_ans(ans, nums[i] + nums[j] + nums[k], target);
                if (t < target) {
                    while (j < k && nums[j] == nums[j+1]) j ++;
                    j ++;
                    
                }
                else {
                    while (j < k && nums[k] == nums[k-1]) k --;
                    k --;
                }

            }            
        }
        return ans;
    }
    
};
// @lc code=end

