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
    int leastInterval(vector<char>& tasks, int n) {
        int m = tasks.size();
        if (!n) {
            return m;
        }
        vector<int> cnt(30);
        for (char& c : tasks) {
            cnt[c-'A'] ++;
        }
        map<int, int> mp;
        int ans = 0;
        for (int i = 0;m > 0 ;i++) {
            int max_ch = -1, max_v = -1;
            for (int j = 0;j < 26;j++) {
                if (cnt[j] > 0 && cnt[j] > max_v && (mp.count(j) == 0 || i - mp[j] > n)) {
                    max_ch = j;
                    max_v = cnt[j];
                }
            }
            // printf("select %d, v %d m %d\n", max_ch, max_v, m);
            if (max_ch != -1) {
                cnt[max_ch] --;
                m --;
                mp[max_ch] = i;
            }
            
            ans ++;
        }
        return ans;
    }
};


int main() {

    return 0;
}