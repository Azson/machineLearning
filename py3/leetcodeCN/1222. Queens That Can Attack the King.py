class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """

        def ok(pos):
            if pos[0] == king[0]:
                return 1 if pos[1] > king[1] else 2
            elif pos[1] == king[1]:
                return 3 if pos[0] > king[0] else 4
            elif (pos[1] - king[1]) == (pos[0] - king[0]):
                return 5 if pos[1] > king[1] else 6
            elif (pos[1] - king[1]) == -(pos[0] - king[0]):
                return 7 if pos[1] > king[1] else 8

            return 0

        ans = [None] * 8
        for item in queens:
            ret = ok(item)
            if ret:
                ret -= 1
                if not ans[ret] or \
                    abs(item[0] - king[0]) + abs(item[1] - king[1]) < \
                        abs(ans[ret][0] - king[0]) + abs(ans[ret][1] - king[1]):
                    ans[ret] = item


        return list(filter(lambda x: x != None, ans))