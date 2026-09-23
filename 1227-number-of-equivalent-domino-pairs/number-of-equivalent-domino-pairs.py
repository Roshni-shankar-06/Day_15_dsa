class Solution:
  def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
    ans = 0
    count = [0] * 100  # Keys range from 11 to 99
    
    for a, b in dominoes:
      key = min(a, b) * 10 + max(a, b)
      ans += count[key]
     
