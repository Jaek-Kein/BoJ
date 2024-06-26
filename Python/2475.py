#Question no 2475 검증수
import sys
import math

a,b,c,d,e = map(int, sys.stdin.readline().split())

answer = a*a + b*b + c*c + d*d + e*e

print(answer%10)