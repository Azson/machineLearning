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
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> cnt;
        int n = nums.size();

        for (int & x : nums) {
            if (cnt.count(x) == 0) {
                cnt[x] = 1;
            }
            else {
                cnt[x] ++;
            }
        }
        priority_queue<pair<int, int>, vector<pair<int, int> > > pqe;
        for (auto & [k, v] : cnt) {
            pqe.push(make_pair(v, k));
        }
        vector<int> ans;
        while (k--) {
            auto [k, v] = pqe.top();
            pqe.pop();
            ans.push_back(v);
        }
        return ans;
    }
};

int main() {

    return 0;
}