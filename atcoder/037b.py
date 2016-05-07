#coding: UTF-8
import sys

N, Q = sys.stdin.readline().split()
res = [0]*int(N)
lists = []

for i in range(int(Q)):
  lists.append(map(int, sys.stdin.readline().split()))

for i in lists:
  for j in range(i[0],i[1]+1):
    res[j-1] = i[2]

for i in res:
  print i
