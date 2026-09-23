class Solution:

  def minOperations(self, nums: list[int], x: int) -> int:
    target = sum(nums) - x
    if target < 0:
      return -1
    if target == 0:
      return len(nums)

    max_len = -1
    cur_sum = 0
    left = 0

    for right in range(len(nums)):
    
