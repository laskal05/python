#cording:UTF-8
import sys

line = map(int, sys.stdin.readline().split())
res = line[2] / min(line[0], line[1])
print res
  
