class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1 # shift right
                else:
                    r = mid - 1 # shift left

            # right sorted portion
            else: 
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1 # shift left
                else:
                    l = mid + 1 # shift right

        return -1