class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        from math import atan2
        from collections import defaultdict


        result = 2
        n = len(points)
        if n == 1:
            return 1
        for i in range(n):
            # print(i)
            gradients = defaultdict(int)
            x1 = points[i][0]
            y1 = points[i][1]
            for j in range(n):
                if j != i:
                    x2 = points[j][0]
                    y2 = points[j][1]

                    y_diff = y2-y1
                    x_diff = x2-x1

                    gradients[atan2(y_diff,x_diff)] += 1
            result = max(result, max(gradients.values()) + 1)
        return result