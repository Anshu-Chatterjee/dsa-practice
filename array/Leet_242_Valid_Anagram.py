# Problem: Valid Anagram (#242)
# Difficulty: Easy
# Pattern: Sorting / String Manipulation
# Time: O(n log n) | Space: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):                 # First, we check if the lengths of the two input strings are different. 
            return False
        if (sorted(s)==sorted(t)):         # If the sorted versions of the strings are equal, it means that they are anagrams of each other, and we can return True.
            return True
        else:
            return False
