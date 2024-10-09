### Problem: [DuplicateInteger](https://neetcode.io/problems/duplicate-integer)
### Solution: hashSet

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # in a hashSet you can not get a duplicate
        hashSet = set()
        for number in nums:
            if number in hashSet:
                return True
            hashSet.add(number)
        return False
```

### Problem: [ValidAnagram](https://neetcode.io/problems/is-anagram)
### Solution: hashMap
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        countS, countT = {}, {}

        for index in range(len(s)):
            # make it so that you split the letter 
            # in a hashmap so later 
            # you can see if all the letters are the same
            countS[s[index]] = 1 + countS.get(s[index], 0)
            countT[t[index]] = 1 + countT.get(t[index], 0)

        return countS == countT
```


### Problem: [TwoSum](https://neetcode.io/problems/two-integer-sum)
### Solution: hashMap
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val : index
        # enumerate until you get a match thats already in the hashMap

        for index, number in enumerate(nums):
            difference = target - number
            if difference in prevMap:
                return [prevMap[difference], index]
            prevMap[number] = index
```


### Problem: [Anagram Groups](https://neetcode.io/problems/anagram-groups)
### Solution: ordinal values and hashMap
```python
class Solution:
    def groupAnagrams(self, strings: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for string in strings:
            count = [0] * 26  # a ... z

            for character in string:
                count[ord(character) - ord("a")] += 1

            result[tuple(count)].append(string)
        return list(result.values())
```


### Problem: [Top K Elements in List](https://neetcode.io/problems/top-k-elements-in-list)
### Solution: bucket sort
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequentie = [[] for i in range(len(nums) + 1)]  # bucket sort

        for number in nums:
            count[number] = 1 + count.get(number, 0)

        for number, counter in count.items():
            frequentie[counter].append(number)

        result = []
        for index in range(len(frequentie) - 1, 0, -1):
            for number in frequentie[index]:
                result.append(number)
                if len(result) == k:
                    return result
```


### Problem: [String Encode and Decode](https://neetcode.io/problems/string-encode-and-decode)
### Solution: none
```python
class Solution:
    # encode the word by making it decodable later
    # put the lenght of the word in front with a indicator of when the word starts in this case #
    def encode(self, strings: List[str]) -> str:
        encoded_string = ""
        for word in strings:
            encoded_string += str(len(word)) + "#" + word
        return encoded_string

    def decode(self, string: str) -> List[str]:
        decoded_list = []  # This is the list that will hold the decoded words
        index = 0
        while index < len(string):
            j = index

            # Find the '#' to get the length of the word
            while string[j] != "#":
                j += 1
            length = int(string[index:j])  # Get the length of the word

            # Extract the word after '#' with a slice
            word = string[j + 1 : j + 1 + length]

            # Append the extracted word to decoded_list
            decoded_list.append(word)

            # Move index to the next word's length indicator
            index = j + 1 + length

        return decoded_list
```


### Problem: [Products of Array Discluding Self](https://neetcode.io/problems/string-encode-and-decode)
### Solution: Prerequisites
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    result = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        result[1] = prefix
        prefix *= nums[i]
    postfix = 1

    for i in range(len(nums)-1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result
```

### Problem: [valid sudoku](https://neetcode.io/problems/string-encode-and-decode)
### Solution: hashMaps
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colums = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)# key = row//3 , colum//3

        for row in range(9):
            for colum in range(9):
                boardNumber = board[row][colum]

                if boardNumber == ".":
                    continue

                if (boardNumber in rows[row] or
                    boardNumber in colums[colum] or
                    boardNumber in squares[row // 3, colum // 3]):
                    return False

                colums[colum].add(boardNumber)
                rows[row].add(boardNumber)
                squares[row // 3, colum // 3].add(boardNumber)
        return True
```

### Problem: [Longest Consecutive Sequence](https://neetcode.io/problems/string-encode-and-decode)
### Solution: set
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numberSet = set(nums)
        highestStreak = 0

        # looping trough the set is faster then the array 
        # because of duplicates
        for number in numberSet:
            if (number - 1) not in numberSet:
                streak = 1
                while (number + streak) in numberSet:
                    streak += 1
                highestStreak = max(streak, highestStreak)
        return highestStreak
```