class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,max_length,max_freq=0,0,0
        smap = {}

        for r in range(len(s)):
            smap[s[r]] = 1 + smap.get(s[r],0)
            max_freq = max(smap.values())
            while r - l + 1 - max_freq > k:
                smap[s[l]]-=1
                l+=1
            max_length = max(max_length, r-l+1)

        return max_length
        