def brute_force(limit):
  first = 1
  second = 1
  total = 0
  while True:
    third = first + second
    if third > limit:
      return total
    if third % 2 == 0:
      total += third
    first = second
    second = third

def solve(limit):
  if limit < 2:
    return 0
  elif limit < 8:
    return 2
  elif limit < 34:
    return 10
  first = 2
  second = 8
  total = 10
  while True:
    third = first + 4*second
    if third > limit:
      return total
    total += third
    first = second
    second = third

def test(limit, correct=None):
  if correct is None:
    correct = brute_force(limit)
  return solve(limit) == correct

assert test(5)
assert test(10)
assert test(4000000, 4613732)
print('All tests passed')