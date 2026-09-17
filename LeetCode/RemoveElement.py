def removeElement(nums, val):
  """
  :type nums: List[int]
  :type val: int
  :rtype: int
  """
  total = 0
  for i in range(len(nums) -1, -1, -1):
    if nums[i] == val:
      total += 1
      nums.pop(i)

  return total

x = removeElement([0,1,2,2,3,0,4,2], 3)
print()