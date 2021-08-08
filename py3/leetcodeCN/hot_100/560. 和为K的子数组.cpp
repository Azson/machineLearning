# include <cstdio>
# include <stack>
# include <vector>
# include <algorithm>
# include <queue>
# include <cstring>
# include <map>

using namespace std;


class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        int ans = 0, sm = 0;
        unordered_map<int, int> cnt;
        cnt[0] = 1;

        for (int i = 0;i < n;i++) {
            sm += nums[i];
            if (cnt.count(sm - k)) {
                ans += cnt[sm-k];
            }
            cnt[sm] ++;
        }
        return ans;
    }
};


int main() {

    return 0;
}