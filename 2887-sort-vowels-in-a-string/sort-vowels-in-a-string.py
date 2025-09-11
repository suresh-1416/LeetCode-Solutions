class Solution:
    def sortVowels(self, s: str) -> str:
        vowels_set ="AEIOUaeiou"
        c=0
        s_list=list(s)
        vowels = [c for c in s if c in vowels_set]
        vowels.sort()
        if vowels == []:
            return s
        for i in range(len(s_list)):
            if s_list[i] in vowels_set:
                s_list[i]=vowels[c]
                c+=1
        return "".join(s_list)