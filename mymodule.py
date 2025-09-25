amt=10000
def balance():
    print("YOUR BANK BALANCE IS $",amt)
def withdraw():
    n=int(input("ENTER THE AMOUNT TO WTIHDRAW: "))
    print("YOUR AMOUNT HAS BEEN DEBITED.")
    print("YOUR BALANCE AMOUNT IS: $",amt-n)
def deposit():
    n=int(input("ENTER THE AMOUNT TO BE DEPOSITED"))
    print("YOUR AMOUNT HAS BEEN CREDITED")
    print("YOUR BALANCE AMOUNT IS: $",amt+n)
def exite():
    print("THANK YOU VISIT AGAIN")
