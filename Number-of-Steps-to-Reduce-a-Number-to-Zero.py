# Problem:
# Given a non-negative integer num, return the number of steps to reduce it to zero.
# If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

Solution:
class Solution:
    def numberOfSteps (self, num: int) -> int:
        print(num)
        # if num%2 == 0:
        #     num = int(num/2)
        # else:
        #     num = int(num-1)
        # print(num)
        count = 0
        while num > 0:
            count +=1
            if num%2 == 0:
                num = int(num/2)
            else:
                num = int(num-1)
        # print(count)
        return count
