# include <cstdio>
# include <string>
# include <vector>
# include <algorithm>

using namespace  std;


class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     * 返回在所有合法的三角形的组成中，最大的三角形的周长减去最小的三角形的周长的值
     * @param n int整型 代表题目中的n
     * @param a int整型vector 代表n个数的大小
     * @return int整型
     */
    typedef long long LL;
    bool is_ok(int a, int b, int c) {
        if (a+b > c && a+c > b && b+c > a &&
            b-a < c && c-a < b && c-b < a)
            return true;
        return false;
    }
    int solve(int n, vector<int>& a) {
        // write code here
        sort(a.begin(), a.end());
        int mx = -1;
        for (int i = n-3;i >= 0;i++) {
            if (is_ok(a[i], a[i+1], a[i+2])) {
                mx = a[i] + a[i+1] + a[i+2];
                break;
            }
        }
        LL mn = 1e15;
        for (int i = 2;i < n && (LL)a[i]*2 < mn;i++) {
            for (int j = 0, k;j < i && (LL)a[i]+a[j]*2 < mn;j++) {
                for (k = j+1;k < i && (LL)a[i]+a[j]+a[k] < mn;k++) {
                    if (is_ok(a[j], a[k], a[i])) {
                        mn = min(mn, (LL)a[i] + a[j] + a[k]);
                    }
                }

            }
        }
        return mx-mn;
    }
};


int main(int argc, char const *argv[])
{
    Solution obj = Solution();
    vector<int> a;
    a.push_back(2); a.push_back(2); a.push_back(2);
    printf("%d\n", obj.solve(3, a));
    return 0;
}
