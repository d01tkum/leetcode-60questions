class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for index, num in enumerate(nums): # O(n)
            # If duplicated numbers are included in 'nums', only the biggest index is recorded to 'indices'
            indices[num] = index
        
        for index, num in enumerate(nums): # O(n)
            diff = target - num
            if diff in indices.keys() and indices[diff] != index:  # O(1)
                return [index, indices[diff]]
        return [-1, -1]
