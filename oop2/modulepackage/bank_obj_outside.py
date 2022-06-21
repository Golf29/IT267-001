#this file is outside bank package
#call module
#from customer import customer
#from account import Account
#from bank import customer,account
#cus1 = customer.customer()
#cus1_acc = account.Account()

from bank.customer import customer
from bank.account import Account

cus1 = customer()
cus1.new_customer()

cus1_acc = Account()
cus1_acc.open_account(cus1.name,"Saving",'10-123-456',500)

print("**** Open Bank Account Detail ****")
print(cus1.cus_info())
print(cus1_acc.display_balance())