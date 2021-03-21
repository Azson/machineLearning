# include <cstdio>
# include <vector>
# include <string>
# include <cstring>
# include <algorithm>
# include <stack>
# include <queue>
# include <set>

using namespace std;

typedef long long LL;

LL cost(int& val, LL res) {
    LL ret;
    if (res >= val -1) {
        ret = (LL)(val-1) * val / 2 + (res-val+1);
    }
    else {
        ret = (LL)res * (2*val - res - 1) / 2;
    }
    return ret;
}


class Solution {
public:
    bool ok(int val, int& n, int& index, int& maxSum) {
        LL left, right, res;
        // cal left
        res = n - index - 1;
        left = cost(val, res);
        // cal right
        res = index;
        right = cost(val, res);

        if (left + right + val <= maxSum) {
            return true;
        }

        return false;
    }
    int maxValue(int n, int index, int maxSum) {

        int l = 1, r = maxSum, m, ans = 0;
        while (l <= r) {
            m = (l+r) / 2;
            if (ok(m, n, index, maxSum)) {
                l = m + 1;
                ans = max(ans, m);
            }
            else {
                r = m-1;
            }
        }
        return ans;
    }
};


int main() {

    return 0;
}