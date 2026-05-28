# Problem: Top K Frequent Elements (#347)
# Difficulty: Medium
# Pattern: Hash Map / Sorting
# Time: O(n² + m log m) | Space: O(m)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numSet=set(nums)
        numSet=list(numSet)
        l1=[]
        mydict={}
        for i in numSet:
            current=nums.count(i)      # We create a set of unique numbers from the input list and then iterate through this set to count the frequency of each number in the original list. We store these frequencies in a dictionary where the keys are the unique numbers and the values are their corresponding counts.
            mydict[i]=current
        sortDict=dict(sorted(mydict.items(), key=lambda item: item[1], reverse=True))
        l2=list(sortDict)
        for i in range(0,k):
            l1.append(l2[i])         # We then sort the dictionary by its values (the frequencies) in descending order and extract the keys (the unique numbers) into a list. Finally, we take the first k elements from this sorted list of unique numbers and return them as the result.
        return l1
