#
# 返回所求中序序列
# @param n int整型 二叉树节点数量
# @param pre int整型一维数组 前序序列
# @param suf int整型一维数组 后序序列
# @return int整型一维数组
#

'''
[3, 2, 1, 4, 5]
[1, 5, 4, 2, 3]
[1, 2, 5, 4, 3]
'''

class Solution:
    def solve(self , n , pre, suf):
        # write code here
        import sys
        sys.setrecursionlimit(100005)
        
        ans = [0] * n
        ans_c = 0
        
        def do_tree(pl, pr, sl, sr):
            nonlocal ans_c, ans
            if pr < pl: return
            if pl == pr: 
                ans[ans_c] = pre[pl]
                ans_c += 1
                return
            pos = dt[pre[pl+1]]
            do_tree(pl+1, pos-sl+pl+1, sl, pos-1)
            ans[ans_c] = pre[pl]
            ans_c += 1
            do_tree(pos-sl+pl+2, pr, pos+1, sr)
        
        dt = dict()
        for i, item in enumerate(suf):
            dt[item] = i
        do_tree(0, n-1, 0, n-1)
        return ans

            

if __name__ == "__main__":
    
    n , pre, suf = 5,[3,2,1,4,5],[1,5,4,2,3]
    # n, pre, suf = 1, [1], [1]
    s = Solution()
    print(s.solve(n , pre, suf))