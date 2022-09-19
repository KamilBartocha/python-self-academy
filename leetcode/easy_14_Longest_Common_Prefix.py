# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

from ast import List

class Solution:
    def longestCommonPrefix(strs):
        prefix = strs[0]
        def find_prefix(word_1, word_2):
            match = ""
            for i in range(min(len(word_1), len(word_2))):
                # flower flow -> 0 1 2 3 
                if word_1[i] == word_2[i]:
                    match = match + str(word_1[i])
                else: return match
            return match
        
        for idx in range(len(strs) - 1 ):
            prefix = find_prefix(prefix, strs[idx + 1])
        
        return prefix    


    strs = ["flower","flow","flight"]
    strs2 = ["dog","racecar","car"]
    strs3 = ["cir","car"]
    longestCommonPrefix(strs)
    longestCommonPrefix(strs2)
    longestCommonPrefix(strs3)
