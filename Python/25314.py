a = int (input())
long = "long "
line = "long " 
for i in range (1, a//4):
    line = line + long
   
if a%4 == 0 :
    print (line + "int")
else :
    print (line + long + "int")
