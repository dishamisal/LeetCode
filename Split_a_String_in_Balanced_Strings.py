# Problem:
# Balanced strings are those who have equal quantity of 'L' and 'R' characters.
# Given a balanced string s split it in the maximum amount of balanced strings.
# Return the maximum amount of splitted balanced strings.

# Example:
# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

# Solution:
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # print(s)
        # print("L", s.count('L'))
        # print("R",s.count('R'))
        # for i, j in enumerate(s):
        #     print(i, j)
        final_list = []
        counter1 = 0
        counter2 = 0
        sub = ''
        for i in s:
            sub += i
            # print(sub)
            if i == 'R':
                counter1 += 1
            else:
                counter2 += 1
            if counter1 == counter2:
                final_list.append(sub)
            # print(len(final_list))
        return len(final_list)
