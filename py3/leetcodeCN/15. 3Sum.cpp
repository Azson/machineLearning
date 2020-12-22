# include <cstdio>
# include <vector>
using namespace  std;

class Solution {
public:
    vector<vector<int> > threeSum(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int> > ans;
        
        sort(nums.begin(), nums.end());

        for (int i = 0, k;i < n;i++) {
            if (i && nums[i] == nums[i-1])
                continue;
            k = n-1;
            for (int j = i+1;j < n;j++) {
                if (j > i+1 && nums[j] == nums[j-1])
                    continue;
                while (j < k && nums[i] + nums[j] + nums[k] > 0)    k--;
                if (j >= k) {
                    break;
                }
                if (nums[i] + nums[j] + nums[k] == 0) {
                    vector<int> tmp;
                    tmp.push_back(nums[i]); tmp.push_back(nums[j]); tmp.push_back(nums[k]);
                    ans.push_back(tmp);
                    //printf("%d %d %d\n", nums[i], nums[j], nums[k]);
                }
            }
        }
        return ans;
    }
};


int main(int argc, char const *argv[])
{
    Solution obj = Solution();
    vector<int> a;
    // [-1,0,1,2,-1,-4]
    // [[-1,-1,2],[-1,0,1]]
    a.push_back(-1); a.push_back(0); a.push_back(1);
    a.push_back(2); a.push_back(-1); a.push_back(-4);
    obj.threeSum(a);
    return 0;
}
