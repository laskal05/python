#cording:UTF-8
import sys

line = sys.stdin.readline().split()

smaller = int(line[0])
if smaller > int(line[1]):
  smaller = int(line[1])
res = int(line[2]) / smaller
print res
  
