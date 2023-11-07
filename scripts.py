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

# Word Order
from collections import OrderedDict
ordered_dictionary = OrderedDict()
n = int(input())
for i in range(n):
    w = str(input())
    if w not in ordered_dictionary:
        ordered_dictionary[w] = 1
    else:
        prev_price = ordered_dictionary[w]
        ordered_dictionary[w] = int(prev_price) + 1
print(len(ordered_dictionary))
ret = ""
for key, value in ordered_dictionary.items():
    ret = ret + str(value) + ' '
print(ret)

# Collections.deque()
from collections import deque
d = deque()
n = int(input())
for i in range(n):
    l = input().split()
    if l[0] == "append":
        d.append(l[1])
    elif l[0] == "appendleft":
        d.appendleft(l[1])
    elif l[0] == "pop" and len(d) != 0:
        d.pop()
    elif l[0] == "popleft" and len(d) != 0:
        d.popleft()
ret = ""
for el in d:
    ret = ret + str(el) + " "
print(ret)

# Company Logo
import math
import os
import random
import re
import sys
from collections import Counter
if __name__ == '__main__':
    s = list(input())
    s.sort()
    sc = Counter(s)
    for el in sc.most_common(3):
        res = el[0] + ' ' + str(el[1])
        print(res)

# Piling Up!
t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    flag = True
    elem = max(l[0], l[-1])
    for i in range(len(l)):
        if (l[0] > l[-1]) and (l[0] <= elem):
            elem = l[0]
            l.pop(0)
        elif (l[0] <= l[-1]) and (l[-1] <= elem):
            elem = l[-1]
            l.pop(-1)
        else:
            flag = False
            break
    if flag == False:
        print("No")
    else:
        print("Yes")

# Calendar Module
import calendar
date = list(map(int, input().split()))
nd = calendar.weekday(date[2], date[0], date[1])
print(calendar.day_name[nd].upper())

# Exceptions
n = int(input())
for i in range(n):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)

# Athlete Sort
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    res = sorted(arr, key = lambda item: item[k])
    for i in res:
        print(*i)

# ginortS
s = str(input())
la = []
ua = []
on = []
dn = []
for el in s:
    if el.isalpha():
        if el.islower():
            la.append(el)
        else:
            ua.append(el)
    elif el.isdecimal():
        if (int(el) % 2 != 0):
            on.append(el)
        elif (int(el) % 2 == 0): 
            dn.append(el)
la.sort()
ua.sort()
on.sort()
dn.sort()
print("".join(la + ua + on + dn))

# Map and Lambda Function
cube = lambda x: x**3
def fibonacci(n):
    if n==0:
        return []
    elif n == 1:
        return [0]
    l = [0, 1]
    for i in range(n-2):
        l.append(l[i]+l[i+1])
    return l

# Detect Floating Point Number
import re
n = int(input())
for i in range(n):
    s = str(input())
    print(bool(re.fullmatch(r'^[+/-]?[0-9]*[.][0-9]+', s)))

# Re.split()
regex_pattern = r"[,.]+" # Do not delete 'r'.

# Group(), Groups() & Groupdict()
s = input()
p = ''
flag = False
for i in s:
    if i.isalnum():
        if i == p:
            flag = True
            break
        else:
            p = i
if flag:
    print(p)
else:
    print(-1)
    
# Re.findall() & Re.finditer()
import re
o = re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])', input())
if o:
    for el in o:
        l = []
        for i in range(0, len(el)):
            l.append(el[i])
        print(''.join(l))
else:
    print(-1)

# Re.start() & Re.end()
import re
s = input()
k = input()
o = re.search(k, s)
res = []
if not o:
    print("(-1, -1)")
else:
    while o:
        start_index = o.start()
        end_index = o.end() -1
        res.append('(' + str(start_index) + ', ' + str(end_index) + ')')
        s = s.replace(s[start_index], "0", 1)
        o = re.search(k, s)
    res = list(set(res))
    res.sort()
    for el in res:
        print(el)

# Regex Substitution
import re
n = int(input())
for i in range(n):
    s = input()
    while ' && ' in s:
        s = re.sub(r" && ", " and ", s)
    while ' || ' in s:
        s = re.sub(r" \|\| ", " or ", s)
    print(s)

# Validating Roman Numerals
regex_pattern = r"^(M){0,3}(CM)?(D)?(CD)?(C){0,3}(XC)?(L)?(XL)?(X){0,3}(IX)?(V)?(IV)?(I){0,3}$"	# Do not delete 'r'.

# Validating phone numbers
import re
n = int(input())
for i in range(n):
    if re.fullmatch(r"[7/8/9](\d){9}", input()):
        print("YES")
    else:
        print("NO")

# Validating and Parsing Email Addresses
import re
import email.utils
n = int(input())
for i in range(n):
    s = input()
    n, e = email.utils.parseaddr(s)
    res = re.match(r'^[a-zA-Z]+[\w.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$', e)
    if n != '' and res:
        print(n, " <", e, ">", sep='')

# Hex Color Code
import re
n = int(input())
for i in range(n):
    s = input()
    res = re.findall(r'(?:.)(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', s)
    if res:
        for el in res:
            print(el)

# HTML Parser - Part 1
from html.parser import HTMLParser
n = int(input())
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if attrs:
            for el in attrs:
                print("->", el[0], ">", el[1])     
    def handle_endtag(self, tag):
        print("End   :", tag)
        
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if attrs:
            for el in attrs:
                print("->", el[0], ">", el[1])
parser = MyHTMLParser()
for i in range(n):
    s = input()
    parser.feed(s)

# HTML Parser - Part 2
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
            print(data)
        else:
            print(">>> Single-line Comment")
            print(data)
    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)
html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
parser = MyHTMLParser()
parser.feed(html)
parser.close()

# Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for attr in attrs:
                print('->', attr[0], '>', attr[1])
    def handle_startendtag(self, tag, attrs):
        print(tag)
        if attrs:
            for attr in attrs:
                print('->', attr[0], '>', attr[1])
p = MyHTMLParser()
n = int(input())
for i in range(n):
    s = input()
    p.feed(s)

# Validating UID
n = int(input())
for i in range(n):
    nu = 0
    nd = 0
    s = input().strip()
    ls = len(s)
    s1 = set(s)
    if ls != 10 or ls != len(s1):
        print("Invalid")
        continue
    for c in s:
        if c.isalnum():
            if c.isdigit():
                nd = nd + 1
            elif c.isalpha() and c.isupper():
                nu = nu + 1
        else:
            print("Invalid")
            break
    if nu < 2 or nd < 3:
        print("Invalid")
    else:
        print("Valid")

# Validating Credit Card Numbers
import re
n = int(input())
for i in range(n):
    c = input()
    cp = re.sub('-', '', c)
    if (re.fullmatch(r'^[4|5|6]\d{3}-?\d{4}-?\d{4}-?\d{4}', c) and not re.findall(r'(.)\1{3}', cp)):
        print("Valid")
    else:
        print("Invalid")

# Validating Postal Codes
regex_integer_in_range = r"^[1-9]\d{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.

# Matrix Script
import math
import os
import random
import re
import sys
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
dec = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
for i in range(m):
    for j in range(n):
        dec.append(matrix[j][i])
s = ''.join(dec)
pat = r'\b([!@#$\%& ]+)\b'
res = re.sub(pat, " ", s)
print(res)

# XML 1 - Find the Score
def get_attr_number(node):
    c = 0
    c += len(node.attrib)
    for el in node:
        c += get_attr_number(el)
    return c

# XML2 - Find the Maximum Depth
maxdepth = 0
def depth(elem, level):
    global maxdepth
    level = level + 1
    if level > maxdepth:
        maxdepth = level
    for e in elem:
        depth(e, level)

# Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        sl = []
        for el in l:
            el = el[-10:]
            sl.append(el)
        sl.sort()
        for el in sl:
            el1 = str(el[:5])
            el2 = str(el[5:])
            print('+91 ' + el1 + ' ' + el2)
    return fun

# Decorators 2 - Name Directory
def person_lister(f):
    def inner(people):
        people.sort(key=lambda x: int(x[2]))
        return [f(i) for i in people]
    return inner

# Arrays
def arrays(arr):
    a = numpy.array(arr, float)
    res = numpy.flipud(a)
    return res

# Shape and Reshape
import numpy as np
n = np.array(input().split(), int)
n.shape = (3, 3)
print(n)
 
# Transpose and Flatten
import numpy as np
n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(np.array(input().split(), int))
res = np.array(l)
print(res.transpose())
print(res.flatten())

# Concatenate
import numpy as np
n, m, p = map(int, input().split())
l1 = []
l2 = []
for i in range(n):
    l1.append(np.array(input().split(), int))
for i in range(m):
    l2.append(np.array(input().split(), int))
a1 = np.array(l1)
a2 = np.array(l2)
res = np.concatenate((a1, a2), axis = 0)
print(res)

# Zeros and Ones
import numpy as np
n = list(map(int, input().split()))
print(np.zeros(n, dtype=int))
print(np.ones(n, dtype=int))

# Eye and Identity
import numpy as np
np.set_printoptions(legacy='1.13')
n, m = map(int, input().split())
print(np.eye(n, m))

# Array Mathematics
import numpy as np
n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    l = np.array(input().split(), int)
    a.append(l)
for i in range(n):
    l = np.array(input().split(), int)
    b.append(l)
A = np.array(a)
B = np.array(b)
print(np.add(A, B))
print(np.subtract(A, B))
print(np.multiply(A, B))
print(np.floor_divide(A, B))
print(np.mod(A, B))
print(np.power(A, B))

# Floor, Ceil and Rint
import numpy as np
np.set_printoptions(legacy='1.13')
a = np.array(list(map(float, input().split())), float)
print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))

# Sum and Prod
import numpy as np
n, m = map(int, input().split())
a = []
for i in range(n):
    l = np.array(list(map(int, input().split())), int)
    a.append(l)
A = np.array(a)
s = np.sum(A, axis = 0)
print(np.prod(s, axis = 0))

# Min and Max
import numpy as np
n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(np.array(input().split(), int))
a1 = np.array(l)
a2 = np.min(a1, axis=1)
print(np.max(a2))

# Mean, Var, and Std
import numpy as np
n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(np.array(input().split(), int))
a = np.array(l)
print(np.mean(a, axis=1))
print(np.var(a, axis=0))
print(round(np.std(a), 11))

# Dot and Cross
import numpy as np
n = int(input())
a = []
b = []
for i in range(n):
    a.append(np.array(input().split(), int))
A = np.array(a)
for i in range(n):
    b.append(np.array(input().split(), int))
B = np.array(b)
print(np.dot(A, B))

# Inner and Outer
import numpy as np
A = np.array(input().split(), int)
B = np.array(input().split(), int)
print(np.inner(A, B))
print(np.outer(A, B))

# Polynomials
import numpy as np
p = np.array(input().split(), float)
n = int(input())
print(np.polyval(p, n))

# Linear Algebra
import numpy as np
n = int(input())
a = []
for i in range(n):
    a.append(np.array(input().split(), float))
A = np.array(a)
print(round(np.linalg.det(A), 2))

# Birthday Cake Candles
import math
import os
import random
import re
import sys
def birthdayCakeCandles(candles):
    m = max(candles)
    n = 0
    for el in candles:
        if (el == m):
            n = n + 1
    return n
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()

# Number Line Jumps
import math
import os
import random
import re
import sys
def kangaroo(x1, v1, x2, v2):
    if (v2 >= v1):
        return "NO"
    if ((x2 - x1) % (v1 - v2) == 0):
        return "YES"
    return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()

# Viral Advertising
import math
import os
import random
import re
import sys
def viralAdvertising(n):
    c = 0
    p = 5
    for i in range(n):
        c = c + p//2
        p = p//2 * 3
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    result = viralAdvertising(n)
    fptr.write(str(result) + '\n')
    fptr.close()

# Recursive Digit Sum
import math
import os
import random
import re
import sys
def superDigit(n, k):
    if k == 1 and len(n) == 1:
        return n
    s = str(sum(list(map(int, n))) * k)
    return superDigit(str(sum(list(map(int, s)))), 1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()

# Insertion Sort - Part 1
import math
import os
import random
import re
import sys
def insertionSort1(n, arr):
    num = arr[n -1]
    for i in range(n-1, -1, -1):
        if (arr[i-1] > arr[i]):
            arr[i] = arr[i-1]
            print(*arr)
            arr[i-1] = num
            if arr == sorted(arr):
                print(*arr)
                break
        else:
            arr[i]= arr[i-1]
            arr[i-1] = arr[i]
            print(*arr)
            if arr == sorted(arr):
                break
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)

# Insertion Sort - Part 2
import math
import os
import random
import re
import sys
def insertionSort2(n, arr):
    for i in range(1, n):
        el = arr[i]
        if el < arr[i-1]:
            for j in range(i, 0, -1):
                if el < arr[j-1]:
                    arr[j] = arr[j-1]
                    arr[j-1] = el
                else:
                    break
        print(*arr)
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)
