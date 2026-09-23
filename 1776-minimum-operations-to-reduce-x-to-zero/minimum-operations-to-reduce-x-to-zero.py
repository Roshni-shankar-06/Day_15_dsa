class Solution:

  def minOperations(self, nums: list[int], x: int) -> int:
    target = sum(nums) - x
    if target < 0:
    
