class BalanceException:
  pass

class BankAccount:
  no_of_customers=0
  def __init__(self,name,initialAmount):
    self.name=name
    self.balance=initialAmount
    BankAccount.no_of_customers+=1

  def getbalance(self):
    print(f'balannce of {self.name} is {self.balance}')

  def deposit(self,amount):
    self.balance+=amount
    self.getbalance()
  
  def isviable(self,amount):
    if self.balance>=amount:
      return 
    else:
      raise BalanceException(print("balance not enough"))
  def withdraw(self,amount):
    try:
      self.isviable(amount)
      self.balance-=amount
      print("withdraw complete")
      self.getbalance()
    except BalanceException as e:
      print('withdraw incomplete',e)
  
  def transfer(self,amount,account):
    try:
      self.isviable(amount)
      self.withdraw(amount)
      account.deposit(amount)
      print('transfer complete')
    except BalanceException as e:
      print("transfer interrupted", e)
     

class InterestReward(BankAccount):
  def __init__(self,name,initialAmount,interestRate):
    super().__init__(name,initialAmount)
    self.rate=interestRate

  def deposit(self, amount):
    self.balance+=amount+((self.rate/100)*amount)
    self.getbalance()

class SavingAccount(InterestReward):
  def __init__(self, name, initialAmount, interestRate,fee):
    super().__init__(name, initialAmount, interestRate)
    self.fee=fee
  
  def withdraw(self, amount):
    try:
      self.isviable(amount+self.fee)
      self.balance-=(amount+self.fee)
      print("withdraw complete")
      self.getbalance()
    except BalanceException as e:
      print('withdraw incomplete',e)
    
      

    



