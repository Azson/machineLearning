# include <cstdio>
# include <algorithm>
# include <string>
# include <map>


using namespace std;


class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     * 返回符合题意的最长的子串长度
     * @param x string字符串 
     * @return int整型
     */
    bool ok(map<char, int>& mp) {
        if (mp['n'] == 0 || mp['p'] == 0 || mp['y'] == 0) 
            return true;

        return false;
    }
    int Maximumlength(string x) {
        // write code here
        int n = x.length();
        int ans = 0;
        int l, r;
        l=r=0;
        map<char, int> mp;
        while (l <= r && r < n) {
            while (r < n) {
                if (mp.count(x[r]) > 0)
                    mp[x[r]] ++;
                else {
                    mp[x[r]]  = 1;
                }
                r ++;
                if (!ok(mp)) {
                 
                    ans = max(ans, r-l-1);
                    //mp[x[r-1]] --;
                    break;
                }

            }
            //printf("- l %d, r %d, n %d\n", l, r, n);
            while (!ok(mp)) mp[x[l++]] --;
            //printf("l %d, r %d, n %d\n", l, r, n);
        }
        ans = max(ans, r-l);
        return ans;
    }
};


int main()
{
    Solution obj = Solution();
    printf("%d\n", obj.Maximumlength("abcdefghijklmn"));
    return 0;
}