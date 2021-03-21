#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 
# @param n string字符串 三角形的长和高
# @return bool布尔型
#
class Solution:
    def judge(self , n ):
        # write code here
        n = int(n)
        return n&(n+1) == 0