class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Idea: prefix_products[i] = product of everything before i
        prefix_products = [0] * n
        # Suffix products is similar, just after i instead of before
        suffix_products = [0] * n
        # Set each one's first/last item to 1, multiplicative identity
        prefix_products[0] = 1
        suffix_products[-1] = 1
        for i in range(1, n):
            prefix_products[i] = prefix_products[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suffix_products[i] = suffix_products[i+1] * nums[i+1]
        return [
            prefix * suffix
            for prefix, suffix in zip(prefix_products, suffix_products)
        ]
