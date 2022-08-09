class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        total_weight_on_left, total_weight_on_right = 0, sum(nums)

        for idx, current_weight in enumerate(nums):

            total_weight_on_right -= current_weight

            if total_weight_on_left == total_weight_on_right:
                return idx

            total_weight_on_left += current_weight

        return -1