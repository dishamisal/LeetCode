# Problem:
# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Solution:
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        final = []
        parts = len(nums) / n
        import numpy as np
        split_list = np.array_split(nums, parts)
        # print(split_list[0])
        # print(split_list[1])
        # print(split_list[0][0])
        for one, two in zip(split_list[0], split_list[1]):
            # print(one, two)
            final.append(one)
            final.append(two)
        print(final)
        return(final)
