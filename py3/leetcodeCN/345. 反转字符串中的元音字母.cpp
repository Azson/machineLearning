# include <cstdio>
# include <stack>
# include <vector>
# include <algorithm>
# include <queue>
# include <string>
# include <map>

using namespace std;


class Solution {
public:
    bool is_alpha(char ch) {
        int v;
        if (ch >= 'a' && ch <= 'z') {
            v = ch - 'a';
        } else {
            v = ch - 'A';
        }
        vector<int> test {'a', 'e', 'i', 'o', 'u'};
        for (int i = 0;i < 5;i++) {
            if (v == test[i] - 'a') {
                return true;
            }
        }
        return false;
    }
    string reverseVowels(string s) {
        int n = s.length();
        int l = 0, r = n - 1;
        
        while (l < r) {
            while (l < r && !is_alpha(s[l])) {
                l ++;
            }
            while (r > l && !is_alpha(s[r])) {
                r --;
            }
            if (l < r) {
                swap(s[l], s[r]);
                l ++;
                r --;
            }
        }
        return s;
    }
};


int main() {

    return 0;
}