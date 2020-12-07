list1 = [1,2,3,4,5]

list1[0]
list1[4]
list1[-1]

list1[1:4]

list2 = range (1,6,1)

list3 = range(1,10,2)

print(list2[0],list2[1],list2[2],list2[3],list2[4])

print(list3[0],list3[1],list3[2],list3[3],list3[4])

a = range (0,10,1)

print(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9])

b = range (0,10,2)

print(b[0],b[1],b[2],b[3],b[4])
      
c = range (5,11,2)

print(c[0],c[1],c[2])

d = range (0,-10,-1)

print(d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8],d[9])

for i in range(5):
    print('Hello')
    
########
    
sum=0

for i in range(1,11,1):
    
    sum=sum+i

print("總共",sum)
##########
sum= 0
for i in range(2,11,2):
    sum = sum + i
print("總共",sum)
#########
sum = 0
for i in range (3,14,3):
    sum = sum+i
print("總共",sum)