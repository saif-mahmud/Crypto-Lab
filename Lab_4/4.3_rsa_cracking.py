import sys
from fractions import Fraction as frac
from math import gcd, floor
from isqrt import isqrt
sys.setrecursionlimit(10**4)
# text=int(open("4.3_ciphertext.hex").read())
e=int(open("4.4_public_key.hex").read(),0)
n=int((open("4.5_modulo.hex").read()),0)
p = 0
q = 0

# print(text,"\n",e,"\n",n)

def validate(x):
    k = x.numerator
    d = x.denominator
    totient = frac(e * d - 1, k)
    if (n - totient + 1) ** 2 - 4 * n < 0:
        return False, None, None,None
    D = isqrt(((n - totient + 1) ** 2 - 4 * n).numerator)
    if D * D != (n - totient + 1) ** 2 - 4 * n:
        return False, None, None,None
    x = ((n - totient + 1) + (D)) / (2)
    y = ((n - totient + 1) - (D)) / (2)
    v = False
    if x == floor(x):
        v = True
    return v, x, y,d


def extendedEuclid(l, s):
    if s == 0:
        return (1, 0, l)
    x, y, d = extendedEuclid(s, l % s)
    return (y, x - floor(l / s) * y, d)


def value(x):
    sum = x[len(x) - 1]
    for i in range(len(x) - 2, -1, -1):
        sum = frac(1, sum) + x[i]
    return sum


def cont(r):
    i = floor(r)
    f = r - frac(i, 1)
    if f == frac(0, 1):
        return [i]
    return ([i] + cont(frac(1, f)))


def bigmod(x, y, p):
    if y == 1:
        return x % p
    if y % 2 == 1:
        return ((x % p) * bigmod((x*x)%p, y//2, p) )% p
    return (bigmod((x*x)%p, y//2, p)) % p


x=cont(frac(e,n))
for i in range(len(x)):
    c = (value(x[:i + 1]))
    if c != 0 and c.denominator % 2 != 0:
        v, p, q, d = validate(c)
        if v:
            break
totient = (p - 1) * (q - 1)
d2, y, z = extendedEuclid(e, totient)
# print(d==d2)
# m = bigmod(text, d, n)
print("Private Key:",d,d==d2,p*q==n)
# print("Message:",m)
