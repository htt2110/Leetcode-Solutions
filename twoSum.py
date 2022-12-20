'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

    ### Naive Solution ###
def twoSumNaive(nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j: 
                    continue
                else:
                    sum_num = nums[i] + nums[j]        
                if sum_num == target:
                    return [i,j]
                else:
                    continue

   ### Hash Map Solution ###
def twoSumOptmized(nums, target):
        required = {}
        for i in range(len(nums)):
            if target - nums[i] in required:
                return [required[target - nums[i]],i]
            else:
                required[nums[i]]=i


