# Problem:
# We are given a list nums of integers representing a list compressed with run-length encoding.
# Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0). 
# For each such pair, there are freq elements with value val concatenated in a sublist.
# Concatenate all the sublists from left to right to generate the decompressed list.
# Return the decompressed list.

Solution:
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        dict = {}
        for i, j in enumerate(nums):
            if i % 2 == 0:
                val = j
            else:
                freq = j
                dict[freq] = val
                lis = []
                for k, v in dict.items():
                    lis = [k] * v
                    print(lis)
                    # for i in lis:
        lis1 = []
        lis_final = []
        for k, v in dict.items():
            # lis1.append([k] * v)
            lis1 = lis1 + ([k] * v)
            print(lis1)
        return lis1
