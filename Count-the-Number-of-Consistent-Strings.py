# Problem:
# You are given a string allowed consisting of distinct characters and an array of strings words.
# A string is consistent if all characters in the string appear in the string allowed.
# Return the number of consistent strings in the array words.

# Solution:
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        print(allowed)
        set_ = set(allowed)
        counter = 0
        for i in words:
            subset = set(i)
            if subset == set_:
                counter += 1
        print(counter)
        return counter
