# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 2:01:58 2022

@author: ajit
"""

# a) Created a database with required attributes: Account no. | Name | DOB | Address | Bank balance.
database = [[1234,'Ajit', '16.04.1998', 'Berhampur, Odisha', 23000 ],
            [4367,'Auro', '15.08.1996', 'Kolkota, West Bengal', 34000 ],
            [3456,'Sandy', '10.08.1998', 'Solahpur, UP', 45000 ]]

print(database)

# b) Insert a new account to the database.
from operator import itemgetter 
print('Enter details for a new account.')

accNo = int(input('Enter account number: '))

flag = True

while(flag):
    for customer in database:
        if(customer[0] == accNo):
            print('Customer already has an account!')
            accNo = int(input('Re-enter account number: '))
            break
    else:
        flag = False

name = input('Enter customer name:')
DOB = input('Enter date of birth(dd.mm.yyyy):')
address = input('Enter address:')
balance = int(input('Enter account balance:'))
newAcc = [accNo, name, DOB, address, balance]

database.append(newAcc)
database = sorted(database, key = itemgetter(1))

print('\nDatabase with the new element.')
print(database)

# c) Delete a customer's details with respect to account number.
accNo = int(input('Enter account number to be deleted:'))

for customer in database:
    if customer[0]==accNo:
        database.remove(customer)
        break
else:
    print('Customer details not found!')

print('\nDatabase after the deleted entry.')
print(database)
    
# d) Take customer details and append at the beggining of the database.
accNo = int(input('Enter account number: '))
name = input('Enter customer name:')
DOB = input('Enter date of birth(dd.mm.yyyy):')
address = input('Enter address:')
balance = int(input('Enter account balance:'))
newAcc = [accNo, name, DOB, address, balance]
    
database.insert(0,newAcc)
        
print(database)

# e) identify duplicates and remove all but one with respect to account number.

i = 0
while i<len(database):
    j = i+1
    while j<len(database):
        if database[i][0] == database[j][0]:
            database.remove(database[j])
        j = j+1
    i = i+1

print('\nDatabase with unique elements:')
print(database)            

# f) sort the bank accounts alphabetically.
database = sorted(database, key = itemgetter(1))
print('\nDatabase with sorted elements:')
print(database)            

