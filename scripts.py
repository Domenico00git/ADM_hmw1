# Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")

# Python If-Else
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
    if (n%2 != 0):
        print("Weird")
    elif (n>=2 and n<=5):
        print("Not Weird")
    elif (n>=6 and n<=20):
        print("Weird")
    elif (n>=20):
        print("Not Weird")
        
# Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
    
# Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if (a != 0):
        print(a//b)
        print(a/b)
# Loops
if __name__ == '__main__':
    n = int(input())
    i = 0;
    while (i<n):
        print(i**2)
        i = i+1
        
# Write a function
def is_leap(year):
    leap = False
    if (year % 4 == 0):
        leap = True
    if (year % 100 == 0):
        leap = False
        if (year % 400 == 0):
            leap = True
    return leap

# Print Function
if __name__ == '__main__':
    n = int(input())
    string = ""
    for i in range(1, n+1):
        string = string + str(i)
    print (string)

# List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l = [[a, b, c] for a in range (0, x +1) for b in range (0, y +1) for c in range(0, z +1) if (a +b +c != n)]
    print (l)

# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lista = list(arr)
    m = max(lista)
    r = lista.count(m)
    for i in range (r): 
        lista.remove(m)
    print(max(lista))
            
# Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    somma = 0
    for el in student_marks[query_name]:
        somma = somma + el
    res = somma / 3
    print("%.2f" % res)

# Nested Lists
if __name__ == '__main__':
    lista = []
    lvoti = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista.append([name, score])
        lvoti.append(score)
    minimo = min(lvoti)
    nmin = lvoti.count(minimo)
    for i in range (nmin):
        lvoti.remove(minimo)
    minimo = min(lvoti)
    nmin = lvoti.count(minimo)
    ret = []
    for i in range (len(lista)):
        el = lista[i]
        if el[1] == minimo:
            ret.append(el[0])
    ret.sort()
    for el in ret:
        print(el)

# Lists
if __name__ == '__main__':
    N = int(input())
    lista = []
    res = []
    for i in range (N):
        lista.append(input())
    for el in lista:
        el = el.split()
        if el[0] == 'insert':
            res.insert(int(el[1]), int(el[2]))
        elif el[0] == 'print':
            print(res)
        elif el[0] == 'remove':
            res.remove(int(el[1]))
        elif el[0] == 'append':
            res.append(int(el[1]))
        elif el[0] == 'sort':
            res.sort()
        elif el[0] == 'pop':
            res.pop()
        elif el[0] == 'reverse':
            res.reverse()

# Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(list(integer_list))
    print(hash(t))

# sWAP cASE
def swap_case(s):
    string = ''
    for l in s:
        la = ord(l)
        if la >= 65 and la <= 90:
            la = la + 32
        elif la >=97 and la <= 122:
            la = la - 32
        string = string + chr(la)
    return string

# String Split and Join
def split_and_join(line):
    l = line.split(" ")
    res = "-".join(l)
    return res
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# What's Your Name?
def print_full_name(first, last):
    print("Hello ", first, " ", last, "! You just delved into python.", sep="")

# Mutations
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    res = ''.join(l)
    return res

# Find a string
def count_substring(string, sub_string):
    count = 0
    for i in range (0, len(string)):
        j = 0
        if string[i] == sub_string[j]:
            j = j +1
            for k in range (i+1 ,len(string)):
                if j == (len(sub_string) - 1 ) and string[k] == sub_string[j]:
                    count = count + 1
                    break
                if string[k] != sub_string[j]:
                    break
                j = j+1
    return count

# String Validators
if __name__ == '__main__':
    s = input()
    flag = False    
    for i in range (0, len(s)):
        if s[i].isalnum():
            flag = True
            break
    print(flag)
    flag = False 
    for i in range (0, len(s)):
        if s[i].isalpha():
            flag = True
            break
    print(flag)
    flag = False
    for i in range (0, len(s)):
        if s[i].isdigit():
            flag = True
            break
    print(flag)
    flag = False
    for i in range (0, len(s)):
        if s[i].islower():
            flag = True
            break
    print(flag)
    flag = False
    for i in range (0, len(s)):
        if s[i].isupper():
            flag = True
            break
    print(flag)
    flag = False

# Text Wrap
def wrap(string, max_width):
    res = ""
    for i in range (1, len(string) + 1):
        res = res + string[i-1]
        if i % max_width == 0 or i == len(string):
            res = res + "\n"
    return res

# Text Alignment
n = int(input())
width = 2*n - 1
res = ""
for i in range (1, n*2, 2):
    res = 'H'*i
    print (res.center(width, ' '))
res = ""
for i in range (0,n + 1):
    res ='H'*n
    print (res.rjust(n + (width-n)//2,' ') + res.rjust((n*4), ' '))
res = ""
for i in range (0, n, 2):
    res = 'H'*n*5
    print(res.rjust(n*5 + (width-n)//2, ' '))
res = ""
for i in range (0,n + 1):
    res = 'H'*n
    print(res.rjust(n + (width-n)//2, ' ') + res.rjust((n*4), ' '))
res = ""
for i in range (1, n*2, 2):
    res = 'H'*(n*2-i)
    print (res.center(width*5+4, ' '))

# Capitalize!
def solve(s):
    res = ""
    for i in range(len(s)):
        if (i == 0 or (i != ' ' and s[i-1] == ' ')):
            res = res + s[i].upper()
        else:
            res = res + s[i]
    return res

# Introduction to Sets
def average(array):
    s = set(array)
    n = len(s)
    l = list(s)
    return (sum(l)/n)

# No Idea!
n, m = map(int, input().split())
l = list(input().split())
A = set(input().split())
B = set(input().split())
h = 0
for num in l:
    if num in A:
        h += 1
    elif num in B:
        h -= 1
print(h)

# Symmetric Difference
m = int(input())
l1 = set(map(int, input().split()))
n = int(input())
l2 = set(map(int, input().split()))
l3 = l1.intersection(l2)
res = l1.union(l2)
res = res.difference(l3)
ris = list(res)
ris.sort()
for el in ris:
    print (el)

# Set .add()
n = int(input())
res = set('')
for i in range(n):
    res.add(input())
print(len(res))

# Set .union() Operation
n = int(input())
l1 = map(int, input().split())
m = int(input())
l2 = map(int, input().split())
s1 = set(l1)
s2 = set(l2)
res = s1.union(s2)
print(len(res))

# Set .intersection() Operation
n = int(input())
l1 = map(int, input().split())
m = int(input())
l2 = map(int, input().split())
s1 = set(l1)
s2 = set(l2)
res = s1.intersection(s2)
print(len(res))

# Set .discard(), .remove() & .pop()
m = int(input())
for i in range (m):
    l2 = input().split()
    if l2[0]=="remove":
        if int(l2[1]) in s1:
            s1.remove(int(l2[1]))
    elif l2[0]=="discard":
        s1.discard(int(l2[1]))
    elif l2[0]=="pop":
        l = list(s1)
        l.reverse()
        l.pop()
        l.reverse()
        s1 = set(l)
print(sum(s1))

# Set .difference() Operation
n = int(input())
l1 = map(int, input().split())
m = int(input())
l2 = map(int, input().split())
s1 = set(l1)
s2 = set(l2)
res = s1.difference(s2)
print(len(res))

# Set .symmetric_difference() Operation
n = int(input())
l1 = map(int, input().split())
m = int(input())
l2 = map(int, input().split())
s1 = set(l1)
s2 = set(l2)
s3 = s1.intersection(s2)
res = s1.union(s2)
res = res.difference(s3)
print(len(res))

# Set Mutations
n = int(input())
l1 = map(int, input().split())
s1 = set(l1)
m = int(input())
for i in range(m):
    l2 = input().split()
    l3 = map(int, input().split())
    s3 = set(l3)
    if l2[0] == "intersection_update":
        s1.intersection_update(s3)
    elif l2[0] == "update":
        s1.update(s3)
    elif l2[0] == "symmetric_difference_update":
        s1.symmetric_difference_update(s3)
    elif l2[0] == "difference_update":
        s1. difference_update(s3)
print(sum(s1))

# Check Subset
n = int(input())
for i in range (n):
    nA = int(input())
    lA = map(int, input().split())
    nB = int(input())
    lB = map(int, input().split())
    sA = set(lA)
    sB = set(lB)
    if len(sA.difference(sB)) == 0:
        print(True)
    else:
        print(False)

# Check Strict Superset
l1 = list(map(int, input().split()))
s1 = set(l1)
n = int(input())
flag = True
for i in range(n):
    l2 = list(map(int, input().split()))
    s2 = set(l2)
    if (len(s1.difference(s2)) == 0 or len(s2.difference(s1)) != 0):
        flag = False
print(flag)

# collections.Counter()
x = int(input())
l = list(map(int, input().split()))
n = int(input())
tot = 0
for i in range(n):
    if x == 0:
        break
    c = list(map(int, input().split()))
    if c[0] in l:
        tot = tot + c[1]
        l.remove(c[0])
        x = x-1
print(tot)

# DefaultDict Tutorial
from collections import defaultdict
d = defaultdict(list)
n, m = map(int, input().split())
for i in range(1, n + 1 ):
    c = str(input())
    d[c].append(i)
for i in range(m):
    c = str(input())
    res = ""
    if c not in d.keys():
        print(-1)
        continue
    for el in d[c]:
        res = res + str(el) + ' '
    print(res)

# Collections.namedtuple()
from collections import namedtuple
n = int(input())
l = str(input())
NT = namedtuple('NT', l)
s = 0
for i in range(n):
    l1, l2, l3, l4 = input().split()
    t1 = NT(l1, l2, l3, l4)
    s = s + int(t1.MARKS)
print(s/n)

# Collections.OrderedDict()
from collections import OrderedDict
ordered_dictionary = OrderedDict()
n = int(input())
for i in range(n):
    l = input().split()
    price = l.pop()
    s = ' '.join(l)
    if s not in ordered_dictionary:
        ordered_dictionary[s] = int(price)
    else:
        prev_price = ordered_dictionary[s]
        ordered_dictionary[s] = int(prev_price) + int(price)
for key, value in ordered_dictionary.items():
    print(key, value)

# 

