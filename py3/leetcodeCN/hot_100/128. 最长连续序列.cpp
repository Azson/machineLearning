# include <cstdio>
# include <stack>
# include <vector>
# include <algorithm>
# include <queue>
# include <cstring>

using namespace std;


class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> st;
        for (auto & x : nums) {
            st.insert(x);
        }
        int n = nums.size();
        int ans = 0, tmp;
        for (auto x : nums) {
            if (!st.count(x - 1)) {
                tmp = 1;
                while (st.count(x+1)) {
                    x ++;
                    tmp ++;
                }
                ans = max(ans, tmp);
            }
            
        }
        return ans;
    }
};

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int ans = n?1:0, tmp = 1;
        for (int i = 0;i < n;i++) {
            while (i+1 < n && nums[i+1] == nums[i]) i ++;
            if (i+1 < n && nums[i+1] - nums[i] == 1) {
                tmp ++;
                ans = max(ans, tmp);
            } else {
                tmp = 1;
            }
            
        }
        return ans;
    }
};


int main() {

    return 0;
}