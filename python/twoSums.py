#!/usr/bin/env python3

from typing import List

class my_dictionary(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value 
  

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        # Create a dict to insert things
        numsDict = my_dictionary()

        numsListLength = len(nums)
        listToReturn = []

        for i in range (numsListLength):
            numsDict.add(i, nums[i])
            
            compliment = target - nums[i]

            if compliment in list(numsDict.values()):

                if list(numsDict.values()).index(compliment) == i:
                    continue

                listToReturn.append(list(numsDict.values()).index(compliment))
                listToReturn.append(i)
                break

        return listToReturn

             

s1 = Solution()
nums1 = [3,3]
print(s1.twoSum(nums1, 6))

nums2 = [3,2,3]
print(s1.twoSum(nums2, 6))


