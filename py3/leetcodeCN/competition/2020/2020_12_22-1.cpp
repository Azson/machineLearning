# include <cstdio>
# include <string>
# include <vector>
# include <algorithm>

using namespace  std;

class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     * 返回m天后高度为奇数的树的数量
     * @param n int整型 
     * @param m int整型 
     * @param l int整型vector 
     * @param r int整型vector 
     * @return int整型
     */
    static const int max_n = 2e5+10;
    int a[max_n];
    int oddnumber(int n, int m, vector<int>& l, vector<int>& r) {
        // write code here
        int ans = 0, c = 0;
        memset(a, 0, sizeof(a));
        for (int i = 0;i < m;i++) {
            a[l[i]-1] --;
            a[r[i]] ++;
        }
        for (int i = n;i > 0;i--) {
            if ((a[i] + m) % 2) {
                ans ++;
            }
            a[i-1] += a[i];
            printf("i %d : %d\n", i, a[i]+m);
        }
        return ans;
    }

};


int main(int argc, char const *argv[])
{
    //4,[0,1,2],[1,2,3],[1,2,2,1]
    Solution obj = Solution();
    int n = 3, m=2;
    vector<int> u, v;
    u.push_back(1); u.push_back(2);
    v.push_back(2); v.push_back(3); 
    //p.push_back(1); p.push_back(2); p.push_back(2); p.push_back(1);
    printf("%d\n", obj.oddnumber(n, m, u, v));
    return 0;
}
