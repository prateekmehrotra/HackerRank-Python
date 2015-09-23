__author__ = 'PrateekMehrotra'
# Enter your code here. Read input from STDIN. Print output to STDOUT
import __builtin__
n = int(raw_input())
T = ()
line = raw_input().split(" ")
for t in range(n):
    T = T + (int(line[t]),)
print(hash(T))

