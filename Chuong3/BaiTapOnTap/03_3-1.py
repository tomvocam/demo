#Tìm SLN bằng if
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
Max= a
if b> Max:
    Max=b
if c> Max:
    Max=c
Min=a
if b<Min:
    Min=b
if c<Min:
    Min=c
print('SLN=',Max)
print('SNN=',Min)
# d=max(a,b,c)
# e=min(a,b,c)
# print(d,e)
