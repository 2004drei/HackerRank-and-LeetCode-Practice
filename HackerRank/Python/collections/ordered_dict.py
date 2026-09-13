from collections import OrderedDict, defaultdict

N = int(input())
myDict = OrderedDict(defaultdict(int))

for _ in range(N):
  i_and_p = input().split()
  item = " ".join(i_and_p[:-1])
  price = int(i_and_p[-1])
  if item in myDict:
    myDict[item] += price
  else:
    myDict[item] = price

for i in myDict:
  print(i, myDict[i])