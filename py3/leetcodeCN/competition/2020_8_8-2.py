#
# 返回牛牛最终是从第几个门进入食堂吃饭的
# @param n int整型 代表门的数量
# @param a int整型一维数组 代表每个门外等待的人数
# @return int整型
#
'''
0 1 2 3
4 5 6 7
k*n + i
'''
class Solution:
    def solve(self , n , a ):
        # write code here
        ln = len(a)
        ans = 1
        ans_c = -1
        for i in range(ln):
            c = (a[i]+n-1-i) // n 
            if ans_c == -1 or c < ans_c:
                ans = i+1
                ans_c = c
        return ans
            


if __name__ == "__main__":
    s = Solution()
    a = [2,3,2,0]
    n = len(a)
    print(s.solve(n, a))