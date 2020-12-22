# include <cstdio>
# include <string>
# include <vector>
# include <algorithm>

using namespace  std;

class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     * 
     * @param n int整型 
     * @return long长整型
     */
    long long wwork(int n) {
        // write code here
        long long ans = n;
        return (long long) (ans+2)*(ans+1)/2;
    }
    long long test(int n) {
        long long ret = 0;
        for (int i = 0; i <= n;i++) {
            for (int j = 0;j <= 1;j++) {
                for (int k = 0;k <= 4;k++) {
                    for (int l = 0;l <= n;l+=2) {
                        for (int m = 0;m <= n;m+=5) {
                            if (i+j+k+l+m == n) {
                                ret ++;
                            }
                        }
                    }
                }
            }
        }
        return ret;
    }
};

int main(int argc, char const *argv[])
{
    //4,[0,1,2],[1,2,3],[1,2,2,1]
    Solution obj = Solution();
    int n = 4;
    for (int i = 1;i <= 10;i++)
    printf("%d -> %lld\n", i, obj.wwork(i));
    return 0;
}
