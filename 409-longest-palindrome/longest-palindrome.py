class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter

        freq = Counter(s)
        cnt = 0
        odd = False
        
        for count in freq.values():
            if count % 2 == 0:
                cnt += count
            else:
                cnt += count - 1
                odd = True
        
        if odd:
            return cnt + 1
        return cnt