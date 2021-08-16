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
    int countArrangement(int n) {
        vector<int> f(1 << n);
        f[0] = 1;
        for (int mask = 1; mask < (1 << n); mask++) {
            int num = __builtin_popcount(mask);
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i) && (num % (i + 1) == 0 || (i + 1) % num == 0)) {
                    f[mask] += f[mask ^ (1 << i)];
                }
            }
        }
        return f[(1 << n) - 1];
    }
};



int main() {

    return 0;
}