from collections import deque

d = deque()
n = int(input())
for i in range(n):
  parts = input().split()
  if len(parts) > 1:
    v = int(parts[1])
  command = parts[0]

  if command == 'append':
    d.append(v)
  elif command == 'pop':
    d.pop()
  elif command == 'popleft':
    d.popleft()
  elif command == 'appendleft':
    d.appendleft(v)
  else:
    pass

print(*d)