# include <cstdio>
# include <string>
# include <vector>

using namespace  std;

class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     * 
     * @param x string字符串 
     * @return int整型
     */
    void go(char c, int& pos, string& x, int& n) {
        if (pos < 0) 
            return ;
        while (pos < n && x[pos] != c)  pos ++;
        
        if (pos < n) 
            pos ++;
        if (pos == n) 
            pos = -1;
    }
    int Maximumlength(string x) {
        int n = x.length(), ans=0;
        int l = 0, r = n-1, mid;
        int pos;
        while (l <= r) {
            mid = (l+r)/2;
            pos = 0;
            for (int i = 0;i < mid;i++) {
                go('a', pos, x, n);
            }
            for (int i = 0;i < mid;i++) {
                go('b', pos, x, n);
            }
            for (int i = 0;i < mid;i++) {
                go('c', pos, x, n);
            }
            //printf("l,r (%d, %d) mid %d, pos %d\n", l, r, mid, pos);
            if (pos < 0) {
                r = mid-1;
            }
            else {
                ans = max(ans, mid);
                l = mid+1;
            }
        }
        return ans*3;
    }
    int Maximumlength_2(string x) {
        // write code here
        int n = x.length(), ans = 0;
        vector<int> pos_a, pos_c;
        vector<int> presum(n+1, 0);
        for (int i = 0;i < n;i++) {
            if (x[i] == 'a')
                pos_a.push_back(i);
            else if (x[i] == 'c')
                pos_c.push_back(i);
            presum[i+1] = presum[i] + (x[i]=='b'?1:0);
        }
        
        reverse(pos_c.begin(), pos_c.end());
        for (int i = 0, ed = min(pos_a.size(), pos_c.size());i < ed;i++) {
            //printf("a %d, c %d, b %d\n", pos_a[i], pos_c[i], presum[pos_c[i]] - presum[pos_a[i]]);
            if (pos_a[i] > pos_c[i])
                break;
            if (presum[pos_c[i]] - presum[pos_a[i]] < i+1)
                break;
            ans ++;
        }
        return ans*3;
    }
};


int main(int argc, char const *argv[])
{
    Solution obj = Solution();
    printf("%d\n", obj.Maximumlength("abaabbcccc"));
    return 0;
}
