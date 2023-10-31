from array import array
from operator import index


y = [2,3,7,5,4]

print(y)
print(len(y))
print(y[0])
print(y[1])
print(y[-1]) #dla pythona
print(y[len(y)-1]) #uniwersalne
print(y[-2])
print(y[0]+y[-1])
print(y[int(len(y)/2)])
print(y[len(y)//2]) # dzielenie bez reszty
# lenght = len(y)
# for i in range(lenght):
#     print(y[i], end=" ")  
# for i in y:
#     print(i, end=" ")
for i in range(len(y)//2+1):
    print(y[i], end=" ")



    
