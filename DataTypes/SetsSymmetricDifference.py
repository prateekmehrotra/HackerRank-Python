__author__ = 'PrateekMehrotra'
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
L1 = raw_input().split(" ")
n = int(raw_input())
L2 = raw_input().split(" ")
L1Set = set(L1)
L2Set = set(L2)
L3 = L1Set.union(L2Set)
L4 = L1Set.intersection(L2)
L5 = L3.difference(L4)
my_list = list(L5)
my_list = [ int(x) for x in my_list ]
my_list.sort()
for s in my_list:
    print(s)
