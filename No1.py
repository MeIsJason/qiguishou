class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            index1 = nums.index(i)
            if target - i in nums[:index1:-1]:
                return [index1, len(nums) - nums[:index1:-1].index(target - i) - 1]


solution = Solution()
print(solution.twoSum([3, 3], 6))

