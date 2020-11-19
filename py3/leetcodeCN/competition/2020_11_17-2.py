#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 
# @param n long长整型 表示标准完全二叉树的结点个数
# @return long长整型
#
class Solution:
    
    def tree4(self , n ):
        # write code here
        def get_deps(x):
            ret = 0
            x += 1
            while x > 0:
                ret += 1
                x = x//2
            return ret
        mod = 998244353
        dep = get_deps(n)
        ans = 0
        res = 0
        if (abs(pow(2, dep) - 1 - n) > 0.000001):
            res = n-pow(2, dep-1)+1
            dep -= 1
        
        for i in range(1, dep+1):
            t = int(pow(2, i-1))
            ans = (ans + (3*t-1)*t//2*i) % mod 

        if res > 0:
            dep += 1
            t = int(pow(2, dep-1))
            ans = (ans + (2*t+res-1)*res//2*dep) %mod 

        return ans


if __name__ == "__main__":
    
    obj = Solution()
    print(obj.tree4(1000000000))