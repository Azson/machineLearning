class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        ret = 0
        ln = len(distance)
        while start != destination:
            ret += distance[start]
            start = (start + 1) % ln

        return min(ret, sum(distance)-ret)