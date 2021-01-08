# Problem:
# You are given a string allowed consisting of distinct characters and an array of strings words.
# A string is consistent if all characters in the string appear in the string allowed.
# Return the number of consistent strings in the array words.

# Example:
# Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# Output: 2
# Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

# Solution:
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        set_ = set(allowed)
        counter = 0
        for i in words:
            subset = set(i)
            if subset.issubset(set_):
                counter += 1
        print(counter)
        return counter
