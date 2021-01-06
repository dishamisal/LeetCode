# Problem:
# Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

Solution:
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
      counter = {}
      for i in arr:
        counter[i] = arr.count(i)
      print(counter)
      values = counter.values()
      return (sorted(values)) == (sorted(list(set(values))))
      
