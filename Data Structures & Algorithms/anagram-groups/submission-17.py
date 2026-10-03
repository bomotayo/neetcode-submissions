class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        smap = {}
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str in smap:
                smap[sorted_str].append(s)
            else: 
                smap[sorted_str] = [s]
        return list(smap.values())