# Problem: Longest Consecutive Sequence (#128)
# Difficulty: Midium
# Pattern: Sorting / Set
# Time: O(n log n) | Space: O(n)
from ast import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        res=1
        count=1
        nums=set(nums)
        nums=list(nums)
        nums.sort()                       # We convert the input list of numbers into a set to remove duplicates and then back to a list to sort it. Sorting the list allows us to easily find consecutive sequences by comparing adjacent elements.
        l=[]
        for i in range(1,len(nums)):
            if(nums[i-1]+1==nums[i]):       # We iterate through the sorted list of numbers and check if the current number is one greater than the previous number. If it is, we increment the count of the current consecutive sequence. If not, we reset the count to 1.
                count=count+1
                res=max(res,count)             # We also update the result variable to keep track of the longest consecutive sequence found so far.
            else:
                count=1                        # If the current number is not one greater than the previous number, we reset the count to 1, indicating the start of a new consecutive sequence.
        return res

