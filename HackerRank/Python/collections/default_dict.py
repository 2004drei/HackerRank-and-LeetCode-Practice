from collections import defaultdict

n, m = map(int, input().split())

positions = defaultdict(list)

for i in range(1, n + 1):
  letter = input()
  positions[letter].append(i)

for _ in range(m):
  letter = input()
  if letter in positions:
    print(*positions[letter])
  else:
    print(-1)