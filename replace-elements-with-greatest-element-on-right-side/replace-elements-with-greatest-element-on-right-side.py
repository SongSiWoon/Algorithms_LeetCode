class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(len(arr)-1):
            res.append(max(list(arr[i+1:])))
        res.append(-1)
        return res
        