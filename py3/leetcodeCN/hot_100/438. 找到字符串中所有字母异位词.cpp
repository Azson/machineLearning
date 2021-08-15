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
    bool ok(vector<int>& a, vector<int>& b) {
        for (int i = 0;i < 26;i++) {
            if (a[i] < b[i]) {
                return false;
            }
        }
        return true;
    }
    vector<int> findAnagrams(string s, string p) {
        vector<int> cnt_s(26), cnt_p(26);
        vector<int> ans;
        int n = p.size(), m = s.size();
        for (int i = 0;i < n;i++) {
            cnt_s[s[i] - 'a'] ++;
            cnt_p[p[i] - 'a'] ++;
        }
        if (ok(cnt_s, cnt_p)) {
            ans.push_back(0);
        }
        for (int i = n;i < m;i++) {
            cnt_s[s[i] - 'a'] ++;
            cnt_s[s[i-n] - 'a'] --;
            if (ok(cnt_s, cnt_p)) {
                ans.push_back(i-n+1);
            }
        }
        return ans;
    }
};


int main() {

    return 0;
}