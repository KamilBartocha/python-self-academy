# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

from ast import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        def match_letters(word1, word2):
            match = ""
            for i in range(min(len(word1), len(word2))):
                if word1[i] != word2[i]:
                    break
            if i != 0:
                match = word1[:i-1]
            return match

        for idx in range(len(strs) - 1):
            prefix = match_letters(prefix, strs[idx + 1])

        return prefix
