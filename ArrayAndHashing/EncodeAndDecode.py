from typing import List

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


solution = Solution()
encoded = solution.encode(["neet", "code", "love", "you"])
print(f"Encoded: {encoded}")

decoded = solution.decode(encoded)
print(f"Decoded: {decoded}")
