# Problem:
# Given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
# Return the shuffled string.

# Example
# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

# Solution:
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        t = tuple(indices + [s])
        # print(t)
        l = []
        for index_, string_ in zip(indices, s):
            t = (index_, string_)
            l.append(t)
        l.sort(key=lambda tup: tup[0])
        # print(l)
        final_string = ""
        for i, j in l:
            # print(j)
            # final_string.append(j)
            final_string = final_string + j
        print(final_string)
        return(final_string)
