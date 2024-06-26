from sys import *
ascending = [1,2,3,4,5,6,7,8]
descending = [8,7,6,5,4,3,2,1]
tone = [*map(int, input().split())]
if tone == ascending:
    print ("ascending")
elif tone == descending :
    print ("descending")
else :
    print ("mixed")

    
