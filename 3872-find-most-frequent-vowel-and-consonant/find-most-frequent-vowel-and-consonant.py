class Solution:
    def maxFreqSum(self, s: str) -> int:
        counts = Counter(s)
        vowels = "aeiou"

        vowel_counts = {ch: cnt for ch, cnt in counts.items() if ch in vowels}
        consonant_counts = {ch: cnt for ch, cnt in counts.items() if ch not in vowels}

        max_vowel_count = max(vowel_counts.values(), default=0)
        max_consonant_count = max(consonant_counts.values(), default=0)
        return max_vowel_count + max_consonant_count
        