#
# ​请返回牛牛能赢的最多局数
# @param n int整型 
# @param p1 int整型 
# @param q1 int整型 
# @param m1 int整型 
# @param p2 int整型 
# @param q2 int整型 
# @param m2 int整型 
# @return int整型
#
class Solution:
    def Mostvictories(self , n , p1 , q1 , m1 , p2 , q2 , m2 ):
        # write code here
        ans = 0
        ans += min(p1, q2)
        ans += min(q1, m2)
        ans += min(m1, p2)
        return ans