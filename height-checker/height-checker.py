class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort_heights = sorted(heights)
        cnt = len(heights)
        for i in range(len(heights)):
            if sort_heights[i] == heights[i]:
                cnt -= 1
        return cnt