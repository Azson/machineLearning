import copy


class node(object):
    def __init__(self):
        self.val = 0
        self.par = 0
        self.lazy = 0
        self.sons = copy.deepcopy([])


class Solution(object):
    def bonus(self, n, leadership, operations):
        """
        :type n: int
        :type leadership: List[List[int]]
        :type operations: List[List[int]]
        :rtype: List[int]
        """

        tree = []
        for i in range(n + 1):
            tree.append(node())
            tree[i].sons = copy.deepcopy([])

        for rel in leadership:
            tree[rel[0]].sons.append(rel[1])
            tree[rel[1]].par = rel[0]

        def chk_status():

            for i in range(1, n + 1):
                print("{0} val:{1} lazy:{2}".format(i, tree[i].val, tree[i].lazy))

        ans = []

        def count_all(x, dp):
            # print("count_all")
            put_up(tree[x].par, dp)

            sum = tree[x].val + tree[x].lazy
            for nd in tree[x].sons:
                sum += count_all(nd, 1)
            return sum

        def put_up(now, dp):
            # print("push_up")
            if not now or not dp:
                return
            # print(now, tree[now].val, tree[now].lazy)
            put_up(tree[now].par, dp - 1)
            tree[now].val += tree[now].lazy
            for nd in tree[now].sons:
                tree[nd].lazy += tree[now].lazy
            tree[now].lazy = 0

        def put_down(x, v):
            tree[x].lazy += v

        for op in operations:
            # print("now op is {0}".format(op))
            if op[0] == 1:
                tree[op[1]].val += op[2]

            elif op[0] == 2:
                put_down(op[1], op[2])

            else:

                ans.append(count_all(op[1], -1))
                # chk_status()

        return ans