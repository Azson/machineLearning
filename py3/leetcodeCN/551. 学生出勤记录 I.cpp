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
    bool checkRecord(string s) {
        int cnt_a, cnt_l, pre = 0;
        cnt_a = cnt_l = 0;
        for (auto & ch : s) {
            if (ch == 'A') {
                if (++cnt_a >= 2) {
                    return false;
                }
            }
            if (ch == 'L') {
                cnt_l ++;
            }
        }
    }
};


int main() {

    return 0;
}