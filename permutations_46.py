class Solution:
    def permute(self, nums):
        res = []

        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return res
# but this is only for integers permutation because it is mutable 
# for in case of strings used below code which first convert string into list and then other approach is same

class Solution:
    def permuteString(self, s: str):
        chars = list(s)
        res = []

        def backtrack(start):
            if start == len(chars):
                res.append("".join(chars))
                return

            for i in range(start, len(chars)):
                chars[start], chars[i] = chars[i], chars[start]
                backtrack(start + 1)
                chars[start], chars[i] = chars[i], chars[start]

        backtrack(0)
        return res
