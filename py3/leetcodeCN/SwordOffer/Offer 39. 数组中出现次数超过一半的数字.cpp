class Solution {
public:
    int majorityElement(vector<int>& nums) {
        // sort(nums.begin(), nums.end());
        // return nums[nums.size()/2];
        int vote = 0, x = -1;
        for (auto& a : nums) {
            if (!vote)  x = a;
            vote += a==x?1:-1;
        }
        return x;
    }
};