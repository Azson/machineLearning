class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {
        int n = nums.size();
        // if (!n)
        int ans = nums[0], sm = nums[0];
        for (int i = 1;i < n;i++) {
            if (nums[i] > nums[i-1]) {
                sm += nums[i];
            }
            else {
                ans = max(ans, sm);
                sm = nums[i];
            }
        }
        
        return max(ans, sm);
    }
};