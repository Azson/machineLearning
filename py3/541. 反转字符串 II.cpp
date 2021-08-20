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
    string reverseStr(string s, int k) {
        int n = s.length();
        for (int i = 0;i < n;i += 2*k) {
            int l = i, r = min(n-1, i+k-1);
            while (l < r) {
                swap(s[l++], s[r--]);
            }
        }
        return s;
    }
};


int main() {

    return 0;
}