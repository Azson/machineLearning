#
# 返回两个区间内各取一个值相乘是p的倍数的个数
# @param a int整型 第一个区间的左边界
# @param b int整型 第一个区间的右边界
# @param c int整型 第二个区间的左边界
# @param d int整型 第二个区间的右边界
# @param p int整型 质数
# @return long长整型
#
class Solution:
    def numbers(self , a , b , c , d , p ):
        # write code here
        t1 = b // p - (a-1) // p
        t2 = d // p - (c-1) // p
        ans = t1 * (d-c+1)
        ans += t2 * (b-a+1)
        ans -= t1*t2

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.numbers(3,7,4,6,3))