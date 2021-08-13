class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cnt = {}
        for s in strs:
            key = ''.join(sorted(s)) 
            if key not in cnt:
                cnt[key] = []
            cnt[key].append(s)
        result = []
        for key in cnt:
            result.append(cnt[key])
     
        return result
                