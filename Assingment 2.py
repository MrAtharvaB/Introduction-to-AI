import math

n = 20

p = 0.5
q = 1 - p

print("Prob. of getting k Heads in 20 tosses:\n")
for k in range(n + 1):
    probability = math.comb(n, k) * (p ** k) * (q ** (n - k))
    print(f"P(X = {k}) = {probability:.5f}")
expected_heads = n * p
expected_tails = n * q
print("\nExpected Number of Heads:", expected_heads)
print("Expected Number of Tails:", expected_tails)
