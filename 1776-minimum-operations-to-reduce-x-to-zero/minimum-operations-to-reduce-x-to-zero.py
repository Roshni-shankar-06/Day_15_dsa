class Solution:

  def minOperations(self, nums: list[int], x: int) -> int:
    target = sum(nums) - x
    if target < 0:
      return -1
    if target == 0:
      return len(nums)

