# bank.py
from account import Account
from utils import load_data, save_data

class Bank:
    def __init__(self):
        self.accounts = self.load_accounts()

    def load_accounts(self):
        data = load_data()
        accounts = {}
        for acc_num, acc_data in data.items():
            acc = Account(acc_data["account_number"], acc_data["password"], acc_data["account_type"], acc_data["balance"])
            acc.loan_balance = acc_data.get("loan_balance", 0)
            accounts[acc_num] = acc
        return accounts

    def save_accounts(self):
        data = {acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}
        save_data(data)

    def create_account(self, account_number, password, account_type="Checking"):
        if account_number in self.accounts:
            print("Account already exists!")
        else:
            self.accounts[account_number] = Account(account_number, password, account_type)
            self.save_accounts()
            print(f"Account {account_number} created successfully.")

    def get_account(self, account_number, password):
        account = self.accounts.get(account_number)
        if account and account.password == password:
            return account
        print("Invalid account number or password.")
        return None

    def deposit(self, account_number, password, amount):
        account = self.get_account(account_number, password)
        if account:
            account.deposit(amount)
            self.save_accounts()
            print(f"Deposited {amount} to account {account_number}. New balance: {account.balance}")

    def withdraw(self, account_number, password, amount):
        account = self.get_account(account_number, password)
        if account:
            try:
                account.withdraw(amount)
                self.save_accounts()
                print(f"Withdrew {amount} from account {account_number}. New balance: {account.balance}")
            except ValueError as e:
                print(e)

    def apply_for_loan(self, account_number, password, loan_amount):
        account = self.get_account(account_number, password)
        if account:
            account.apply_for_loan(loan_amount)
            self.save_accounts()
            print(f"Loan of {loan_amount} granted to account {account_number}. New loan balance: {account.loan_balance}")

    def detect_fraud(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account and amount > 10000:  # Simple threshold-based fraud detection
            print(f"Alert: Large transaction detected for account {account_number}. Amount: {amount}")

    def apply_monthly_interest(self):
        for account in self.accounts.values():
            account.calculate_monthly_interest()
        self.save_accounts()
