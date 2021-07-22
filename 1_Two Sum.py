class Solution(object):
    def twoSum(self, nums, target):
        l=[]
        b=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i==j):
                    continue 
                else:
                    if((nums[i]+nums[j])==target):
                        l.append(i)
                        l.append(j)
                        b=1
            if(b==1):
                break
        print(l)
        return l
        
