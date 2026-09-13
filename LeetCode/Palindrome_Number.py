class Solution():
  def __init__(self, x):
    self.x = x

  def isPalindrome(self):
    n = str(self.x) # n = str(x) in LeetCode
    s = []
    for i in n:
      s.insert(0, i)

    if "".join(s) == n:
      return True
    else:
      return False

num = Solution(input()).isPalindrome()
print(num)