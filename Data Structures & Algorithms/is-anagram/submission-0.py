class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        countS, countT = {}, {}

        for i in range(len(s)):
            if s[i] not in countS:
                countS[s[i]] = 1
            countS[s[i]] += 1
        for j in range(len(t)):
            if t[j] not in countT:
                countT[t[j]] = 1
            countT[t[j]] += 1
        
        return countS == countT