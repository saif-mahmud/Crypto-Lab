from fractions import Fraction
from decimal import *
import math
import sys

sys.setrecursionlimit(1500)

ciphertext = open("4.3_ciphertext.hex", "r").read()
e = open("4.4_public_key.hex", "r").read()
n = open("4.5_modulo.hex", "r").read()

ciphertext = int(ciphertext, 16)
e = int(e, 16)
n = int(n, 16)

d = 1
fractional_parts = []


def getContinuedFractionSum(li):
    a = Fraction(0)
    for i in li:
        b = Fraction(1, 1)
        a = b._div(a._add(i))
    return a


def euclidContinuedFraction(n, e):
    global fractional_parts
    if e == 0:
        return n
    fractional_parts.append(n//e)
    if is_upto_this_approximation_valid(fractional_parts) == True:
        return
    euclidContinuedFraction(e, n % e)


def is_upto_this_approximation_valid(fractional_parts):
    global e
    global n
    global ciphertext
    global d
    rev_fractional_part = list(reversed(fractional_parts))
    rational_approximation = getContinuedFractionSum(rev_fractional_part)
    d = rational_approximation.denominator
    k = rational_approximation.numerator
    if d % 2 == 0 or (e*d-1) % k != 0:
        return False
    phi = (e*d-1)/k
    b = -(n-phi+1)
    determinant = b*b-4*n

    if determinant < 0:
        return False
    # print "n=",n,'\n'
    # print "e",e,'\n'
    # print "d",d,'\n'
    if ((-b+math.sqrt(Decimal(determinant)))/2) % 1 != 0 or ((-b-math.sqrt(Decimal(determinant)))/2) % 1 != 0:
        return False
    # print "got it"
    print bigmod(ciphertext, d, n)
    # print "got it2"
    return True


def bigmod(m, e, n):
    if e == 0:
        return 1
    elif e == 1:
        return m
    elif m == 0 or n == 1:
        return 0
    ans = bigmod(m, (e//2), n) % n
    ans = (ans*ans) % n
    if e % 2 == 1:
        ans = (ans*m) % n
    return ans


euclidContinuedFraction(n, e)
pt = 10101010103
et = bigmod(pt, e, n)
dt = bigmod(et, d, n)
print d
print et, '\n'
print dt
