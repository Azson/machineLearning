class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size(), ans=nums[0];
        vector<int> dp(n+1, 0);
        dp[0] = nums[0]>=0?nums[0]:0;
        for (int i = 1;i < n;i++) {
            if (dp[i-1] <= 0) 
                dp[i] = nums[i];
            else 
                dp[i] = dp[i-1] + nums[i];
            //printf("dp[%d]=%d\n", i, dp[i]);
            ans = max(ans, dp[i]);
        }
        return ans;
    }
};