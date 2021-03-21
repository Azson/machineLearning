# include <cstdio>
# include <cmath>

using namespace std;


class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     * 
     * @param n int整型 
     * @return long长整型
     */
    /*
    sum_i ^n {ceil( n / i)}     i = 1,2,3...
    n + ceil(n/2) + ceil(n/3) + ... + ceil(n/(n-1))  + n/n
    1 + 2 + 2 + ... + n
    ceil (n / (i*i))
    100 / 3 = 34, 100 / 9 = 12
    100 / 2 = 50, 100 / 4 = 25
    100 / 6 = 17
    */
    typedef long long LL;
    long long Sum(int n) {
        // write code here
        LL ans = 1, delta;
        LL cur = 1, left, right, mid, t;
        while (cur < n) {
            delta = ceil((double)n / cur);
            left = cur;
            right = n;
            while (left <= right) {
                mid = (left + right) / 2;
                t = ceil((double)n / mid);
                if (t < delta) {
                    right = mid-1;
                }
                else if (t > delta) {
                    left = mid+1;
                }
                else {
                    break;
                }
                //printf("%lld, %lld = %lld\n", left, right, mid);
            }
            //printf("mid %lld, delta %lld\n", mid, delta);
            ans += (mid-cur+1) * delta;
            cur = mid+1;
            //printf("%lld ans = %lld\n", cur, ans);
        }
        return ans;

    }
};

int main(int argc, char const *argv[])
{
    Solution obj = Solution();
    printf("%lld\n", obj.Sum(3));
    return 0;
}
