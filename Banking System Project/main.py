# main.py
from bank import Bank

def main():
    bank = Bank()
    
    while True:
        print("\n--- Banking System Menu ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Transactions")
        print("5. Apply for Loan")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            account_number = input("Enter new account number: ")
            password = input("Enter password: ")
            account_type = input("Enter account type (Savings/Checking): ")
            bank.create_account(account_number, password, account_type)
        
        elif choice == '2':
            account_number = input("Enter account number: ")
            password = input("Enter password: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(account_number, password, amount)
        
        elif choice == '3':
            account_number = input("Enter account number: ")
            password = input("Enter password: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(account_number, password, amount)
        
        elif choice == '4':
            account_number = input("Enter account number: ")
            password = input("Enter password: ")
            account = bank.get_account(account_number, password)
            if account:
                print("Transaction History:")
                for transaction in account.get_transaction_list():
                    print(transaction)

        elif choice == '5':
            account_number = input("Enter account number: ")
            password = input("Enter password: ")
            loan_amount = float(input("Enter loan amount: "))
            bank.apply_for_loan(account_number, password, loan_amount)
        
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
