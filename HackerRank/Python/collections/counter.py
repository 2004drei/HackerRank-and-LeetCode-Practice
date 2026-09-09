import collections

num_of_shoes = int(input())
sizes_list = collections.Counter(list(map(int, input().split())))
num_of_customers = int(input())
total = 0
for _ in range(num_of_customers):
  size, price = input().split()
  s = int(size)
  p = int(price)
  if sizes_list[s] > 0:
    sizes_list[s] -= 1
    total += p
  else:
    continue

print(total)