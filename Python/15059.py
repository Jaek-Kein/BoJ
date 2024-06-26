#Question No.15059 Hard Choice
from sys import *

menu = list(map(int, input().split())) #the actual amount we have on plane
real = list(map(int, input().split())) #the amount the passanger wants
dif = 0
i = 0
while  i < 3:
    if menu[i] < real[i]:
        dif = dif + menu[i] - real[i]
        i+=1
    else:
        i+=1
        continue

print(dif*-1)