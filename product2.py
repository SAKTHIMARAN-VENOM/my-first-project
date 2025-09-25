import mymodule
print("****************************************")
print("WELCOME TO SAKTHI AND CO BANK")
print("****************************************")
print("1.BALANCE CHECK\n" 
"2.WITHDRAW\n" 
"3.DEPOSIT\n" 
"4.EXIT\n")
n=int(input("ENTER THE NUMBER: "))
if n==1:
    mymodule.balance()
elif n==2:
    mymodule.withdraw()
elif n==3:
    mymodule.deposit()
elif n==4:
    mymodule.exite()
else:
    print("wrong number entered.")
