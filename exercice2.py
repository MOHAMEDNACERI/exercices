U1=[1,2,3,4,5,6,7]
L=[1,0,1,1,5,0,1]
U2=[0]*7
for i in range (7):
   if L[i]==1:
       U2[i]=U1[i]
print(U1)
print(L)
print(U2)