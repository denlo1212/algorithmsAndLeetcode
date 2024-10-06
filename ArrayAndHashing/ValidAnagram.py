class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        countS, countT = {}, {}

        for index in range(len(s)):
            countS[s[index]] = 1 + countS.get(s[index], 0)
            countT[t[index]] = 1 + countT.get(t[index], 0)

        return countS == countT

        # or

    # def isAnagram(self, s: str, t: str) -> bool:
    #     if (len(s) != len(t)):
    #         return False
    #
    #     countS, countT = {}, {}
    #
    #     for index in range(len(s)):
    #         countS[s[index]] = 1 + countS.get(s[index], 0)
    #         countT[t[index]] = 1 + countT.get(t[index], 0)
    #
    #     for character in countS:
    #         if countS[character] != countT.get(character, 0):
    #             return False

solution = Solution()

# Test Case 1: Anagrams
print(solution.isAnagram("anagram", "nagaram"))  # Expected: True

# Test Case 2: Not Anagrams
print(solution.isAnagram("rat", "car"))          # Expected: False
