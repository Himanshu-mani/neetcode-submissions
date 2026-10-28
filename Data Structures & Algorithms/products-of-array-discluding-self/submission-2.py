class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        '''n = len(nums)
        output = [0] * n
        for i in range(0, n):
            product = 1
            for j in range(0, n):
                if i != j:
                    product = product * nums[j]
            output[i] = product
        return output
        '''
        n = len(nums)
        output = [0] * n
        left = 1
        right = 1

        for i in range(n):
            output[i] = left
            left = left * nums[i]
        for i in range(n - 1, -1, -1):
            output[i] = output[i] * right
            right = right * nums[i]
        return output