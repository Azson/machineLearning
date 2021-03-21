class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n == 1:
            return 0
        mp = dict()
        for i in range(n):
            mp[i] = grid[i]
        ans = 0
        for i in range(n-1):
            flag = True if sum(mp[i][i+1:]) == 0 else False

            if flag:
                continue
            for j in range(i+1, n):
                if sum(mp[j][i+1:]) == 0:
                    ans += j-i
                    flag = True
                    tmp = mp[i]
                    
                    for k in range(j, i, -1):
                        mp[k] = mp[k-1]
                    mp[i] = mp[j]
                    break
            
            if not flag:
                return -1
        return ans