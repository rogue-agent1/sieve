#!/usr/bin/env python3
"""sieve — Sieve of Eratosthenes + segmented sieve + prime factorization. Zero deps."""
import sys, time, math

def sieve_of_eratosthenes(n):
    if n < 2: return []
    is_prime = bytearray(b'\x01') * (n + 1)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            is_prime[i*i::i] = bytearray(len(is_prime[i*i::i]))
    return [i for i in range(n + 1) if is_prime[i]]

def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def nth_prime(n):
    if n <= 0: return None
    upper = max(20, int(n * (math.log(n) + math.log(math.log(n)) + 2)))
    primes = sieve_of_eratosthenes(upper)
    while len(primes) < n:
        upper *= 2
        primes = sieve_of_eratosthenes(upper)
    return primes[n - 1]

def main():
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 100
    t0 = time.time()
    primes = sieve_of_eratosthenes(n)
    elapsed = time.time() - t0
    print(f"Primes up to {n}: {len(primes)} found in {elapsed*1000:.1f}ms")
    if len(primes) <= 30:
        print(f"  {primes}")
    else:
        print(f"  First 10: {primes[:10]}")
        print(f"  Last 10:  {primes[-10:]}")
    print(f"\n10th prime: {nth_prime(10)}")
    print(f"100th prime: {nth_prime(100)}")
    for x in [60, 1001, 997]:
        print(f"  Factors of {x}: {prime_factors(x)}")

if __name__ == "__main__":
    main()
