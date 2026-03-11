#!/usr/bin/env python3
"""Sieve of Eratosthenes."""
import sys
n = int(sys.argv[1]) if len(sys.argv)>1 else 100
sieve = [True]*(n+1); sieve[0]=sieve[1]=False
for i in range(2, int(n**0.5)+1):
    if sieve[i]:
        for j in range(i*i, n+1, i): sieve[j]=False
primes = [i for i,v in enumerate(sieve) if v]
print(f"{len(primes)} primes up to {n}")
print(' '.join(map(str, primes)))
