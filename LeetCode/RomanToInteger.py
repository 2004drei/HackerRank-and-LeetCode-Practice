def romanToInt(s):
  romanNums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
  roman = s[::-1]
  newNum = 0
  prev = 0
  for char in roman:
    value = romanNums[char]
    if value < prev:
      newNum -= value
    else:
      newNum += value

    prev = value

  return newNum

n = romanToInt(input())
print(n)