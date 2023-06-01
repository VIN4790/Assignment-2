#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Question 1


# In[ ]:


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sort the list in ascending order
        nums.sort()
        # Initialize sum to zero
        max_sum = 0
        for i in range(0, len(nums), 2):
            # Add every element at even positions (0-indexed)
            max_sum += nums[i]
            
        return max_sum


# In[ ]:


Question 2


# In[ ]:


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:        
        unique_candies = 0        
        for i in range(len(candyType)):           
            for j in range(0, i):               
                if candyType[i] == candyType[j]:
                    break            
            else:
                unique_candies += 1        
        return min(unique_candies, len(candyType) // 2)


# In[ ]:


Question 4


# In[ ]:


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            # Check if the current plot is empty.
            if flowerbed[i] == 0:
                # Check if the left and right plots are empty.
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                # If both plots are empty, we can plant a flower here.
                if empty_left_plot and empty_right_lot:
                    flowerbed[i] = 1
                    count += 1
                    
        return count >= n


# In[ ]:


Question 5


# In[ ]:


import sys
 
# Function to find a maximum
# product of a triplet in array
# of integers of size n
def maxProduct(arr, n):
 
    # if size is less than 3,
    # no triplet exists
    if n < 3:
        return -1
 
    # will contain max product
    max_product = -(sys.maxsize - 1)
     
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                max_product = max(
                    max_product, arr[i]
                    * arr[j] * arr[k])
 
    return max_product
 
# Driver Program
arr = [10, 3, 5, 6, 20]
n = len(arr)
 
max = maxProduct(arr, n)
 
if max == -1:
    print("No Triplet Exits")
else:
    print("Maximum product is", max)
 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




