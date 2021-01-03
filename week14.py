sum = 0
for i in range(2,11,2):
    sum = sum + i
print("Total is", sum)


sum = 0
for i in range(3,13,3):
    sum = sum + i
print("Total is", sum)


n = int(input('輸入'))
sum = 0
for i in range(1,n+1):
  sum+=i**2
print(sum)   
    
people = ["Mario", "Peach", "Luigi", "Daisy", "Toad", "Yoshi"]
dessert = ["Star Pudding", "Peach Pie", "Popsicles", "Honey Cake", "Cookies", "Jelly Beans"]

for i,j in zip(people,dessert):
    

        print('Hi, my name is ',i,'. My favorite dessert is ',j,'.')
