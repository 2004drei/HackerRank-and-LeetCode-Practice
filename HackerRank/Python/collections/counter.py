import collections

num_of_shoes = int(input())
sizes_list = collections.Counter(list(map(int, input().split())))
num_of_customers = int(input())

for i in range(num_of_customers):
  size, price = input().split()
  if sizes_list[int(size)] > 1:
