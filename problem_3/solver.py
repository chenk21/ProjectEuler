def brute_force(n):
  assert n != 0
  while n % 2 == 0:
    n = n >> 1
  max_factor = 2
  i = 3
  while i < n ** 0.5:
    if n % i == 0:
      n = n // i
      max_factor = i
    else:
      i += 2
  return max(max_factor, n)

def solve(n):
  return brute_force(n)

def test(n, correct=None):
  if correct is None:
    correct = brute_force(n)
  return solve(n) == correct

assert test(600851475143, 6857)