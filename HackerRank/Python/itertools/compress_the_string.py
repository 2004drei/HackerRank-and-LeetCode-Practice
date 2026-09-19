from itertools import groupby

s = input()
tupleList = []
for key, group in groupby(s):
  tupleList.append((len(list(group)), int(key)))

print(*tupleList)
