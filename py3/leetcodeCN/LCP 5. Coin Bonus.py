class node(object):
    def __init__(self):
        self.val = 0
        self.par = 0
        self.son_coin = 0
        self.sons = 1
        self.children = []


class Solution(object):
    def bonus(self, n, leadership, operations):
        """
        :type n: int
        :type leadership: List[List[int]]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        MOD = 1000000007
        tree = [node() for i in range(n+1)]

        for rel in leadership:
            tree[rel[1]].par = rel[0]
            #tree[rel[0]].sons += 1
            tree[rel[0]].children.append(rel[1])

        def update_sons(now):
            for son in tree[now].children:
                tree[now].sons += update_sons(son)
            return tree[now].sons


        def push_up(now, val):
            while now:
                tree[now].val += val
                tree[now].val %= MOD
                now = tree[now].par

        update_sons(1)
        ans = []
        for op in operations:

            if op[0] == 1:
                push_up(op[1], op[2])

            elif op[0] == 2:
                tree[op[1]].son_coin += op[2]
                tree[op[1]].son_coin %= MOD

                ret = tree[op[1]].sons*op[2]
                ret %= MOD
                push_up(op[1], ret)

            else:

                ret = tree[op[1]].val
                par = tree[op[1]].par
                while par:
                    ret += tree[par].son_coin * tree[op[1]].sons
                    ret %= MOD
                    par = tree[par].par
                ans.append(ret)

        return ans

if __name__ == '__main__':
    obj = Solution()

    n = 6
    leader = [[1, 2], [1, 6], [2, 3], [2, 5], [1, 4]]
    op = [[1, 1, 500], [2, 2, 50], [3, 1], [2, 6, 15], [3, 1]]

    print(obj.bonus(n, leader, op))