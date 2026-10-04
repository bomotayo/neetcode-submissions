class Solution:
    def isPalindrome(self, s: str) -> bool:
        nstr = ''.join([c.lower() for c in s if c.isalnum()])
        l = 0
        r = len(nstr)-1
        while l <= r:
            if nstr[l] != nstr[r]:
                return False
            l+=1
            r-=1
        
        return True

        