class Solution(object):
    def twoSum(self, nums, target):
        # two point
        nums_index = [(v, index) for index, v in enumerate(nums)]
        nums_index.sort()
        begin, end = 0, len(nums) - 1
        while begin < end:
            curr = nums_index[begin][0] + nums_index[end][0]
            if curr == target:
                return [nums_index[begin][1], nums_index[end][1]]
            elif curr < target:
                begin += 1
            else:
                end -= 1

if __name__ == "__main__":
    # Example usage
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = s.twoSum(nums, target)
    print(f"Indices of numbers that add up to {target}: {result}")
