class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        if (len(s) != len(t)):
            return False

        for index in s:
            countS[[index]] = 1 + countS.get(s[index], 0)
            countT[t[index]] = 1 + countT.get(t[index], 0)

        return countS == countT
