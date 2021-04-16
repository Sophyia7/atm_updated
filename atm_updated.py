


import random
from datetime import datetime #date_time code
dataBase_user = {} #dictionary
accountBalance = 10000

def init():
    
    print('WELCOME!')
    have_account = int(input('Do you have an account with us? 1. Yes 2. No \n'))

    if(have_account == 1):
      login() #directs the user to the login function
    elif(have_account == 2):
      register() #directs the user to the register function
    else:
      print('Invalid input, try again!')

#register function
def register():
  print('*****REGISTER HERE!********')

  user_name = input('What is your name? \n')
  email = input('What is your email address? \n')
  user_password = input('Create a password \n')

  accountNumber = generateAccountNumber() #this calls forth the generated random 10 digit number which is saved  as an account number

  dataBase_user [accountNumber] = [ user_name, email, user_password] #this stores each user details to the dataBase dictionary

  print('Account successfully created!')
  print('Your account number is %d' % accountNumber)
  login()

#this function generates a random 10 digit number
def generateAccountNumber():
  return random.randrange(1111111111,9999999999)

#login function
def login():
  print('***********LOGIN********')
  accountNumberfromUser = int(input('What is your account number? \n'))
  password = input('Enter your password \n')

#this verifies the user making sure that the inputed account number and password aligns with the user details
  for accountNumber, userDetails in dataBase_user.items():
    if(accountNumber == accountNumberfromUser):
      if(userDetails[2] == password):
          print('Welcome')

          bankOperations(userDetails) #after successful login, the user is directed to the bank operations function

    else:
      print('Login failed. Incorrect username and password') #denies access

def bankOperations(user):

  #Shows date & time
  now = datetime.now()
  dt_string = now.strftime('%d/%m/%Y %H:%M:%S')
  print('Date and Time:', dt_string)

  selectedOption = int(input('What would you like to do? 1) Withdrawal 2) Cash deposit 3) Check current balance 4) Transfer 5) Complaint 6) Logout 7) Exit \n'))

  if(selectedOption == 1):
    print('You selected %s' % selectedOption)
    WithdrawalOperation() #directs the user to withdrawal function

  elif(selectedOption == 2):
    print('You selected %s' % selectedOption)
    cashDepositOperation() #directs the user to cash deposit function

  elif(selectedOption == 3):
    print('You selected %s' % selectedOption)
    currentBalanceOperation() #directs the user to current balance function

  elif(selectedOption == 4):
    print('You selected %s' % selectedOption)
    transferOperation() #directs the user to transfer function

  elif(selectedOption == 5):
    print('You selected %s' % selectedOption)
    complaintOperation() #directs the user to complaint function

  elif(selectedOption == 6):
    print('You selected %s' % selectedOption)
    logoutOperation() #directs the user to logout function

  elif(selectedOption == 7):
    print('You selected %s' % selectedOption)
    exitOperation() #directs the user to exit function

  else:
    print('Invalid selection. Try again')


#withdrawal function
def WithdrawalOperation():
  print('Your current balance  is %s' % accountBalance)
  withdrawal = int(input('How do you wish to withdraw? \n'))
  if withdrawal < accountBalance: 
    print('Take cash')

    withdrawal_balance = accountBalance - withdrawal
    print('Your current balance is %s' % withdrawal_balance)
    exitOperation()
  else:
    print('Insufficient funds')
    

#cash deposit function
def cashDepositOperation():
  deposit = int(input('How much do you want to deposit? \n'))
  current_balance = deposit + accountBalance
  print('Your current balance is %s' % current_balance)
  exitOperation()
  

#current balance function
def currentBalanceOperation():
  int(input('Enter account number \n'))
  print('Your current balance  is %s' % accountBalance)
  exitOperation()

#transfer function
def transferOperation():
  input('Enter account number you wish to transfer \n')
  input('Enter amount \n')
  int(input('1. Savings 2. Current \n'))
  print('Successful')
  exitOperation()

#complaint function
def complaintOperation():
  input('What is your complaint \n')
  print('Sent.')
  exitOperation()

#logout function
def logoutOperation():
  login()

#exit function
def exitOperation():
  print('Thank you for choosing us')


    

###SYSTEM INITIALIZING
init()
