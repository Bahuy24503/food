import math


a,b,c,d = map(float,input().split())
S = pow(c-a,2)+pow(d-b,2)
S = math.sqrt(S)
if(S==0) :
    print("0.0000")
    exit(0)
print(round())


