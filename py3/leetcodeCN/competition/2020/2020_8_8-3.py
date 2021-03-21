#
# 
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
    def Highestscore(self , n , p1 , q1 , m1 , p2 , q2 , m2 ):
        # write code here
        t1 = min(p1, q2)
        t2 = min(q1, m2)
        t3 = min(m1, p2)

        ans = t1+t2+t3

        p1 -= t1; q2 -= t1
        q1 -= t2; m2 -= t2
        m1 -= t3; p2 -= t3

        p1 -= min(p1, p2)
        q1 -= min(q1, q2)
        m1 -= min(m1, m2)

        ans -= (p1+m1+q1)

        return ans
