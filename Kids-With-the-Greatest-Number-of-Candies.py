# Problem:
# Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.
# For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them.
# Notice that multiple kids can have the greatest number of candies.

Solution:
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        kids = []
        # print(greatest)
        for i in candies:
            if i + extraCandies >= greatest:
                j = True
                kids.append(j)
            else:
                j = False
                kids.append(j)
        print(kids)
        return kids
