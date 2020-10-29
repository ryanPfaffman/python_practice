 import csv
'''
class Student:
  def __init__(self,name,year, dates):
    self.name = name
    self.year = year
    self.dates = dates
    self.grades = []

  def add_grade(self,grade):
    if type(grade) == Grade:
      self.grades.append(grade)
    else:
      pass


  attendance = {dates: booleans}

roger = Student('Roger van der Weyden',10)
sandro = Student('Sandro Botticelli',12)
pieter = Student('Pieter Bruegel the Elder',8)

class Grade:
  minimum_passing = 65

  def __init__(self, score):
    self.score = score

  def is_passing(self, score):
    if self.score >= minimum_passing:
      return self.score / len(self.grades)

new_score = Grade(100)

pieter.grades.append(new_score)
'''
'''
from collections import defaultdict

def recover_secret(subsequences):
    preceding_chars = defaultdict(set)
    for subseq in subsequences:
        for i in range(len(subseq)):
            preceding_chars[subseq[i]].update(subseq[i - 1] if i else '')

    secret = []
    while preceding_chars:
        c = next(k for k, v in preceding_chars.items() if not v)
        del preceding_chars[c]
        for prec in preceding_chars.values():
            if c in prec:
                prec.remove(c)
        secret.append(c)
    return ''.join(secret)

print(recover_secret([
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]))
'''
'''
from math import gcd

def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

def lcmapp(lst):
    if len(lst) == 2:
        return lcm(lst[0], lst[1])
    else:
        return lcm(lst[0], lcmapp(lst[1:]))

def convertFracts(lst):
    denom = [i[1] for i in lst]
    ans = []
    lcm = lcmapp(denom)
    for i in range(len(lst)):
        ans.append([lcm/denom[i]*lst[i][0],lcm])
    return ans

print(convertFracts([[1, 2], [1, 3], [1, 4]]))
'''


import math



def gap(g, m, p):
    start = 0
    end = 0
    for x in range(m,p+1):
        if is_prime(x):
            if start == 0:
                start = x
            elif end == 0:
                end = x
            else:
                start = end
                end = x
        if end - start == g:
            return [start, end]
    return None

def is_prime(n):
    if n <= 0 or n == 1:
        return False
    i = 2
    while (i <= n ** 0.5 ):
        if n % i == 0:
            return False
        i += 1
    return True


print(gap(6, 100, 110))
