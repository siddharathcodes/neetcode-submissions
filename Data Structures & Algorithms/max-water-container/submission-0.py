class Solution:
    def maxArea(self, height):
        L = 0
        R = len(height) - 1
        maxArea = 0

        while L < R:
            area = (R - L) * min(height[L], height[R])

            maxArea = max(maxArea, area)

            if height[L] < height[R]:
                L += 1
            else:
                R -= 1

        return maxArea