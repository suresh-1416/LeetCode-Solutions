class Solution:
    def canBeTypedWords(self, text: str, b: str) -> int:
        broken = set(b)   # faster lookup
        words = text.split()
        count = 0

        for word in words:
            if not any(ch in broken for ch in word):
                count += 1

        return count
        