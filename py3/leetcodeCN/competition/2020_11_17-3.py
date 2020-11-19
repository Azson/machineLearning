#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回最大和的字符串
# @param x string字符串 即题目描述中所给字符串
# @param k int整型 即题目描述中所给的k
# @return string字符串
#
class Solution:
    def Maxsumforknumers(self , x , k ):
        # write code here
        ls = sorted(x)
        ln = len(ls)
        ans = 0
        for i in range(k-1):
            ans += int(ls[i])
        print(ans)
        ans += int(''.join(ls[k-1:][::-1]))

        return ans


if __name__ == "__main__":
    obj = Solution()
    print(obj.Maxsumforknumers("111222333444555666777888999", 2))
