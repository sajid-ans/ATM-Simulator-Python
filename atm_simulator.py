amount = 1000
def show_Menu():
  print("\n ATM Menu")
  print("1. check balance")
  print("2. Deposite money")
  print("3. Withdraw money")
  print("4. Exit")

def check_Balance():
  print("Your acount Balance is, ",amount) 

def deposite_Money():
  global amount
  balance = int(input("Enter the amount that you want to Deposite\n"))
  if balance <= 0:
    print("Enter valid number\n")
    deposite_Money()
  else:
    amount += balance
    print("Balance ",balance, "has been deposited into your accoount successfully")

def withdraw_Money():
  global amount
  balance = int(input("Enter the amount, want to withdraw\n"))

  if balance > amount:
    print("Insufficent balance")
  else:
    amount -= balance

while True:
  show_Menu() 
  user_input = int(input("Enter number as per your requirement(1-4)\n"))
  #print("yes")
  if user_input==1:
    check_Balance()
  elif user_input==2:
    deposite_Money()
  elif user_input==3:
    withdraw_Money()
  elif user_input==4:
    break
  else:
    print("Please enter the number between 1-4 only")
    continue


