# include <cstdio>
# include <string>
# include <map>
# include <string>
# include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> exchange(vector<int>& nums) {
        int n = nums.size();
        int r = n-1;
        for (int i = 0;i <= r;i++) {
            while (i <= r && nums[i] % 2 == 0) {
                swap(nums[i], nums[r--]);
            }
        }
        //printf("%d\n", r);
        return nums;
    }
};