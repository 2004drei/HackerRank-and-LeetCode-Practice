class Student():
  def __init__(self, name, stud_num):
    self.name = name
    self.stud_num = stud_num
    pass

  def identity(name):
    return f"You're name is {self.name}"

def add1(n):
  return int(n * (n +1) / 2)

def add2(n):
  total_sum = 0
  for i in range (0, n+1):
    total_sum +=i
  return total_sum

print(add1(20))