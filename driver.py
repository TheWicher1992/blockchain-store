from blockchain import *
from wallet import *

class Store:
    def __init__(self):
        self.products = [
        {
            "Name":" Coke",
            "Price":3
        },
        {
            "Name":" Sprite",
            "Price":2
        },
        {
            "Name":" Fanta",
            "Price":5
        },
        {
            "Name":" Lays",
            "Price":4
        },
        {
            "Name":" Cocomo",
            "Price":5
        },
        {
            "Name":" Shawarma",
            "Price":10
        },
        {
            "Name":" Burger",
            "Price":12
        },
        {
            "Name":" Pizza",
            "Price":15
        },
        {
            "Name":" Smoothie",
            "Price":12
        },
        {
            "Name":"Registers",
            "Price":11
        }
        ]
        self.wallet = Wallet()
        
    def print_products(self):
        print("\n----------------------------Welcome to Gotham HyperMart----------------------------")
        print('\nSelect a Product:')
        for i in range(len(self.products)):
            print(str(i+1)+".",self.products[i]['Name'], "\t\tPrice:",self.products[i]['Price'])
        print("\n")

    def select_products(self,buyer_public_key,selection):
        for i in range(len(self.products)):
            drink = self.products[int(selection)]['Name']
            price = self.products[int(selection)]['Price']
            print("\nYou chose to buy",drink,"worth",price,"Gotham Pixels\n")
            break
        return price
        
def print_ledger(wallets, chain):
    print("\n----------------------------Public Ledger----------------------------")
    for wallet in wallets:
        print("Public Key -->",str(wallet.key.public)[0:50]+"...........", "\tGotham Pixels -->", wallet.get_coins(chain))
    print('\n\n')

def print_store_credits(store_wallet, chain):
    print("\n----------------------------Gotham HyperMart----------------------------")
    print("Public Key -->",str(store_wallet.key.public)[0:50]+"...........", "\tGotham Pixels -->", store_wallet.get_coins(chain))
    print('\n\n')

if __name__ == "__main__":   
    A = Wallet()
    chain = Blockchain(1, Transaction('', A.key.public, 500)) 
    B = Wallet()
    C = Wallet()
    D = Wallet()
    E = Wallet()
    store = Store()
    wallets = [A,B,C,D,E]
    print("\n--------------------------WELCOME TO GOTHAM E-COMMERCE BLOCKCHAIN--------------------------")
    print("\n1. View Public Ledger")
    print("2. View Blockchain")
    print("3. View Store Credits")
    print("4. Transfer Credits")
    print("5. Make A Purchase")
    print("6. Immutability Check")
    print("7. Exit\n")
    user_input = input()
    if user_input == '1':
        print_ledger(wallets, chain)
        print("Task Completed Successfully!!!")
        quit("System Shutting Down...\n")
    elif user_input == '2':
        chain.print_chain()
        print("Task Completed Successfully!!!")
        quit("System Shutting Down...\n")
    elif user_input == '3':
        print_store_credits(store.wallet, chain)
        print("Task Completed Successfully!!!")
        quit("System Shutting Down...\n")
    elif user_input == '4':
        A.transfer(200, B.key.public, chain)
        A.transfer(120, C.key.public, chain)
        A.transfer(100, E.key.public, chain)
        A.transfer(40, D.key.public, chain)
        print_ledger(wallets, chain)
        chain.print_chain()
        print("Task Completed Successfully!!!")
        quit("System Shutting Down...\n")
    elif user_input == '5':
        store.print_products()
        selection = input()
        selection = int(selection) - 1
        buy1 = store.select_products(A.key.public,selection)
        A.transfer(buy1, store.wallet.key.public, chain)
        print_ledger(wallets,chain)
        print_store_credits(store.wallet,chain)
        chain.print_chain()
        print("Task Completed Successfully!!!")
        quit("System Shutting Down...\n")
    elif user_input == '6':
        #CHECK FOR WHETHER ERROR HANDLING IS OPERATIONAL
        E.transfer(50, A.key.public, chain)
    elif user_input == '7':
        quit("\nSystem Shutting Down...\n")
    else:
        print("\nINVALID SELECTION\nSECURITY PROTOCOL ACTIVATED!!!\nINIATING SHUTDOWN!!!\n")
        quit()