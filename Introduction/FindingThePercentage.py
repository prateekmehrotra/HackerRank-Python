__author__ = 'PrateekMehrotra'
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
dictionary = {}
for i in range(0,n):
    split = raw_input().split(' ')
    perc = float(split[1]) + float(split[2]) + float(split[3]);
    dictionary[split[0]] = perc/3
student = raw_input()
print("%.2f" % dictionary[student])
