class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        re=[]
        for i in range(len(nums)):
            r=nums[:i]+nums[i+1:]
            t=math.prod(r)
            re.append(t)
        return re