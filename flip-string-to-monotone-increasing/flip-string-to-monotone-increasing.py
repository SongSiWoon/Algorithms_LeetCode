class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        cnt_z = 0
        cnt_o = 0
        
        for i in range(len(s)):
            if s[i] == '0':
                if cnt_o == 0:
                    continue
                cnt_z += 1
            else:
                cnt_o += 1
            cnt_z = min(cnt_z, cnt_o)
        return min(cnt_z, cnt_o)