class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers_set = set()
        for num in nums:
            if num in numbers_set:
                return True
            else:
                numbers_set.add(num)
        
        return False
        


        