List=[]
print('Nhap 10 so nguyen:')
for i in range(10):
    n=int(input())
    List+=[n]#Them phan tu vao List
x=int(input('Nhap x:'))
#Câu A
# for i in range(len(List)):
#     if List[i] == 5:
#         List[i]=x
#Câu B
newlist=[]
for n in List:
    if n != x:
        newlist+=[n]
List=newlist
print(List)


