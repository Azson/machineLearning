# include <cstdio>
# include <string>
# include <vector>
# include <cmath>
# include <algorithm>
# include <queue>

using namespace std;

/*

给出一个仅包含小写字母的字符串s，你最多可以操作k次，使得任意一个小写字母变为与其相邻的小写字母（ASCII码差值的绝对值为1），
请你求出可能的最长相等子序列（即求这个字符串修改至多k次后的的一个最长子序列，且需要保证这个子序列中每个字母相等）。

子序列：从原字符串中取任意多个字母按照先后顺序构成的新的字符串。
*/

class Solution {
public:
    /**
     * 
     * @param k int整型 表示最多的操作次数
     * @param s string字符串 表示一个仅包含小写字母的字符串
     * @return int整型
     */
    
    int string2(int k, string s) {
        // vector<int, vector<int>, greater <int> > a[30];
        int n = s.length();
        int now, t, ans = 1;
        for (int i = 0; i < 26;i++) {
            priority_queue<int, vector<int>, greater <int> > pqe;
            for (int j = 0;j < n;j++) {
                pqe.push(abs(s[j]-'a'-i));
            }
            now = 0;
            t = 0;
            while (!pqe.empty()) {
                //printf("%d\n", pqe.top());
                now += pqe.top();
                pqe.pop();
                
                t ++;
                if (now > k) {
                    t --;
                    ans = max(ans, t);
                    break;
                }
            }
            if (t == n)
                return n;
        }

        return ans;

    }
};

int main(int argc, char const *argv[])
{
    Solution obj = Solution();
    string s1 = "abcde";
    printf("%d\n", obj.string2(2, s1));
    return 0;
}

