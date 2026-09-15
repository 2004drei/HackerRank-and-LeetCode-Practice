from collections import Counter
def longestCommonPrefix(strs):
  """
  :type strs: List[str]
  :rtype: str
  """

  prefixes = Counter()
  if not strs:
    return ""

  prefixes = Counter()
  for word in strs:
    prefixes[word[0:2]] += 1
  
  return max(prefixes, key=prefixes.get)