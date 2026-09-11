from collections import namedtuple
total = 0
N = int(input())
Student = namedtuple('Student', list(input().split()))
for i in range(N):
  s = Student(*list(input().split()))
  total += int(s.MARKS)
print(total / N) 
