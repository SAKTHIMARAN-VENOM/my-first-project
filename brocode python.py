import time
print("WELCOME TO SAKTHI STORES")
food=[]
price=[]
total=0
while True:
    a=input("enter the food u would like to buy(to exit press N): ")
    if a.lower()=="n":
        break
    elif a!="":
        food.append(a)
    else:
       print("you entered a wrong item") 
food.sort()
for i in food:
      b=len(i)
      if b>10:
        price.append(b*100)
      elif b>5 and b<10:
         price.append(b*50)
      else:
        price.append(b*30)
print("your cart will be ready in 10 seconds :")
for j in range(10,0,-1):
    print(j)
    time.sleep(1)
print("------cart---------")
for k in food:     
   print(k,end=" ")
print("\n")
for l in price:
    print("$",l,end=" ")
    total+=l
print("\n")
print("YOUR TOTAL BILL IS : $",total)  
print("---------------------------------") 


  




