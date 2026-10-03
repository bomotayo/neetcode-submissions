class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rmap = {}

        for num in nums:
            rmap[num] = 1 + rmap.get(num,0)
        
        return sorted(rmap,key=lambda r:rmap.get(r), reverse=True)[:k]