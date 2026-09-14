import itertools
s, k = input().split()
k = int(k)
bruh = list(itertools.combinations_with_replacement(sorted(s), k))
for t in bruh:
  combi = ''
  for e in t:
    combi += e
  print(combi)