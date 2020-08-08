#
# 
# @param n int整型 
# @param m int整型 
# @param a int整型一维数组 
# @return int整型
#
class Solution:
    def solve(self , n , m , a ):
        # write code here
        l, r = 0, 0
        ans = -1
        sm = 0
        c = 0
        while l <= r and r < n:
            while c <= m and r < n:
                if a[r] == 0:
                    if c == m:
                        break
                    c += 1
                sm += 1
                r += 1
            # print(l, r, sm, ans, c)
            ans = max(ans, sm)
            if a[l] == 0:
                c -= 1
            sm -= 1
            l += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    # n, m = 6, 2
    # a = [1,0,0,1,1,1]
    n, m = 1, 5
    a = [0] 
    print(s.solve(n, m, a))