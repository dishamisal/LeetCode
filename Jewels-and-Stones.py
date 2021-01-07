# Problem:
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

Solution 1:
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # print(J)
        # print(S)
        counter = 0
        for i in S:
            if i in J:
                counter += 1
        # print(counter)
        return counter
        
Solution 2:
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d = {}
        for i in J:
            d[i] = 0
            counter = 0
        for j in S:
            if j in d:
                counter += 1
        print(counter)
        return counter

