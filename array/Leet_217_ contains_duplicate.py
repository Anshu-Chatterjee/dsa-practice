# Problem: Contains Duplicate (#217)
# Difficulty: Easy
# Pattern: Sorting
# Time: O(n log n) | Space: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==1:         # If the length of the input list is 1, we can immediately return False, as a single element cannot have duplicates.
            return False
        nums.sort()               # We sort the input list in-place, which allows us to easily check for duplicates by comparing adjacent elements.
        for i in range(0,len(nums)-1):  
            if (nums[i]==nums[i+1]):  # We iterate through the sorted list and compare each element with the next one. If we find any two adjacent elements that are the same, it means there is a duplicate, and we can return True.
                return True
        return False
    

# Problem: Contains Duplicate (#217)
# Difficulty: Easy
# Pattern: Hash Set / Lookup
# Time: O(n) | Space: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: 
        if len(nums)==1:
            return False
        if len(set(nums))==len(nums):   # We convert the input list to a set, which will remove any duplicate elements.
            return False                 # If the length of the set is equal to the length of the original list, it means there are no duplicates, and we can return False.
        else:
            return True                  # If the lengths are different, it means there are duplicates, and we can return True.