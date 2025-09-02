class Solution():
    def twoSum(self, nums, target):
            for i in range(len(nums)):
                for p in range(i+1,len(nums)):
                    if nums[i]+nums[p]==target:
                               return[i,p]

                 
     
        
        