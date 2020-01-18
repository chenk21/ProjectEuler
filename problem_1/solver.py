def brute_force(divisors, limit):
  total = 0
  for i in range(1, limit):
    if any(i % d == 0 for d in divisors):
      total += i
  return total

def solve(divisors, limit):
  # Order divisors.
  divisors.sort()
  # Handle trivial case.
  if divisors[0] >= limit:
    return 0
  # Remove divisors which are multiples of others.
  for i in range(len(divisors)):
    for j in range(len(divisors) - 1, i, -1):
      if divisors[j] % divisors[i] == 0:
        divisors.pop(j)
  # 
  total = 0
  for d in divisors:
    total += limit // d
  
  

def test(divisors, limit, correct=None):
  if correct is None:
    correct = brute_force(divisors, limit)
  return solve(divisors, limit) == correct

assert test([3, 5], 10, 23)
assert test([3, 5], 1000, 233168)
print("All tests passed")