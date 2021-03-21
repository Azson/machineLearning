class Solution(object):
    def robot(self, command, obstacles, x, y):
        """
        :type command: str
        :type obstacles: List[List[int]]
        :type x: int
        :type y: int
        :rtype: bool
        """

        op = {
            'U': (0, 1),
            'R': (1, 0)
        }

        ln = len(command)

        circle = [0, 0]
        for i in range(ln):
            circle[0] += op[command[i]][0]
            circle[1] += op[command[i]][1]

        def can_reach(p2):
            det = min(p2[0] // circle[0], p2[1] // circle[1])

            n_x, n_y = det * circle[0], det * circle[1]

            if n_x == p2[0] and n_y == p2[1]:
                return True

            for i in range(ln):
                n_x += op[command[i]][0]
                n_y += op[command[i]][1]

                if n_x == p2[0] and n_y == p2[1]:
                    return True
            return False

        if not can_reach([x, y]):
            return False

        for ob in obstacles:
            if ob[0] >= x and ob[1] >= y:
                continue
            if can_reach(ob):
                return False
        return True

