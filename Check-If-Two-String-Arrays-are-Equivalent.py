# Problem:
# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.

# Example:
# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.

# Solution:
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
      new1 = ""
      for i in word1:
        new1 += i
      print(new1)
      new2 = ""
      for i in word2:
        new2 += i
      print(new2)
        
      return new1 == new2
      
      
      
