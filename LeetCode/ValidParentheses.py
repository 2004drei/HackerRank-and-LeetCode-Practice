def isValid(s):
  """
  :type s: str
  :rtype: bool
  """
  parentheses = {'(': ')', '{': '}', '[': ']'}
  stack = []

  for char in s:
    if char in parentheses:
      stack.append(char)
    else:
      if not stack:
        return False
      if parentheses[stack.pop()] != char:
        return False
  return len(stack) == 0

x = isValid("(){}[]")
print(x)