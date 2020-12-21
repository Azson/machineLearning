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
    // f(x) = 2*f(x/2)+1
    // F(x) = f(1)+f(2)+...+f(x) = n + 2*F(x/2)
    long long Sum(int n) {
        // write code here
        long long  ans = 0, t1 = n, t2 = 1;
        while (t2 <= t1) {
            ans += n/t2 * t2;
            t2 <<= 1;
        }
        
        return ans;
    }
    long long Sum2(int n) {
        long long  ans = 0;
        for (int i = 1;i <= n;i++) {
            ans += i^(i-1);
        }
        return ans;
    }
};


int main(int argc, char const *argv[])
{
    Solution obj = Solution();
    for (int i = 1;i <= 30;i++)
        printf("%d -> %lld cp %lld\n", i, obj.Sum(i), obj.Sum2(i));
    return 0;
}
