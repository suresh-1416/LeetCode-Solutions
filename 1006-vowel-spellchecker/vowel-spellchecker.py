class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        f = lambda x: ''.join('$' if ch in 'aeiou' else ch for ch in x)
        cap, vow = defaultdict(str), defaultdict(str)
        word_set, ans = set(wordlist), []
        
        for w in wordlist:                      # Build the dicts

            wLow = w.lower()
            if not cap[wLow]: cap[wLow] = w     # <–– Case 1: capital-check

            wVow = f(wLow)
            if not vow[wVow]: vow[wVow] = w     # <–– Case 2: vowel-check

        for q in queries:
            qLow, qVow, res = q.lower(), f(q.lower()), ''

            if q in word_set: res = q           # <–– word is in wordlist
            elif qLow in cap: res = cap[qLow]   # <–– cap-checked word is in wordlist
            elif qVow in vow: res = vow[qVow]   # <–– vowel-checked word is in wordlist

            ans.append(res)
        return ans