#1760. Minimum Limit of Balls in a Bag
# Sujal - 25MCA20186
class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """

        left = 1
        right = max(nums)

        while left < right:

            mid = (left + right) // 2
            operations = 0

            for num in nums:
                operations += (num - 1) // mid

            if operations > maxOperations:
                left = mid + 1
            else:
                right = mid

        return left
