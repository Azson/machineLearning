class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """

        ln = len(coordinates)
        if ln >= 2:
            k = [coordinates[0][0] - coordinates[1][0], coordinates[0][1] - coordinates[1][1]]

            for i in range(2, ln):
                if i >= ln:
                    break
                if k[1] * (coordinates[0][0] - coordinates[i][0]) != k[0] * (coordinates[0][1] - coordinates[i][1]):
                    return False
        return True