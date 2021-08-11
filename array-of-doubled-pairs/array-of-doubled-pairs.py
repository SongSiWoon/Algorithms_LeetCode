class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        for i in sorted(arr, key = lambda x: abs(x)):
            if cnt[i] == 0:
                continue
            if cnt[i*2] == 0:
                return False
            cnt[i] -= 1
            cnt[2*i] -= 1
        return True