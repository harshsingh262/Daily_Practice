number = [1,2,3,4,5]
while (n:=len(number))>0:
    print(number.pop())
    
foods=list()
while (food:=input("What foood do you like: ")) !="quit":
    foods.append(food)
print(foods)