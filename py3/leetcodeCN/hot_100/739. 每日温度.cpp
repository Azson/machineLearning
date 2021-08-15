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
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> ans(n);
        stack<pair<int, int> > stk;
        for (int i = 0;i < n;i++) {
            if (!stk.empty() && temperatures[i] > stk.top().first) {
                pair<int, int> now = stk.top();
                stk.pop();
                ans[now.second] = i - now.second;
            }
            stk.push(make_pair(temperatures[i], i));
        }
        return ans;
    }
};


int main() {

    return 0;
}