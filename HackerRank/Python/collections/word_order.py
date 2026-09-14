import collections

n = int(input())
wordsList = []
for i in range(n):
  wordsList.append(input())
count = collections.Counter(wordsList)

print(len(count))
for i in count:
  print(count[i], end=" ")