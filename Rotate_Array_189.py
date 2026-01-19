class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[n-k:] + nums[:n-k]


# or more interview ready approach

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        def rev(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left +=1
                right -=1
        rev(0, n-1)
        rev(0, k-1)
        rev(k, n-1)
