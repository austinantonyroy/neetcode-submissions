class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       c=Counter(nums)
       f=c.most_common(k)
       return [i[0] for i in f]

            



        