# include <cstdio>
# include <string>
# include <map>
# include <string>

using namespace std;


class Solution {
public:
    int firstUniqChar(string s) {
        map<char, int> mp;
        for (auto &c:s) {
            mp[c] ++;
        }
        for (int i = 0, n=s.length();i < n;i++) {
            if (mp[s[i]] == 1) {
                return i;
            }
        }
        return -1;
    }
};