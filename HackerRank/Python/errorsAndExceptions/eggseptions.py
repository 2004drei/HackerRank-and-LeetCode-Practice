
for _ in range(int(input())):
  values = input().split()
  try:
    a = int(values[0])
    b = int(values[1])
    print(a//b)
  except ZeroDivisionError as zde:
    print("Error Code:", zde)
  except ValueError as ve:
    print("Error Code:", ve)
