# account.py
from transaction import TransactionNode

class Account:
    def __init__(self, account_number, password, account_type="Checking", balance=0):
        self.account_number = account_number
        self.password = password
        self.balance = balance
        self.account_type = account_type  # "Savings" or "Checking"
        self.transaction_head = None
        self.loan_balance = 0  # Loan feature
        self.annual_interest_rate = 0.03 if account_type == "Savings" else 0.0

    def deposit(self, amount):
        self.balance += amount
        self._add_transaction("Deposit", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance!")
        self.balance -= amount
        self._add_transaction("Withdrawal", amount)

    def _add_transaction(self, transaction_type, amount):
        transaction_id = len(self.get_transaction_list()) + 1
        new_transaction = TransactionNode(transaction_id, amount, transaction_type)
        new_transaction.next = self.transaction_head
        self.transaction_head = new_transaction

    def get_transaction_list(self):
        transactions = []
        current = self.transaction_head
        while current:
            transactions.append(current.to_dict())
            current = current.next
        return transactions

    def calculate_monthly_interest(self):
        if self.account_type == "Savings":
            monthly_interest = self.balance * (self.annual_interest_rate / 12)
            self.deposit(monthly_interest)

    def apply_for_loan(self, loan_amount, interest_rate=0.05):
        self.loan_balance += loan_amount * (1 + interest_rate)
        self._add_transaction("Loan Granted", loan_amount)

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "password": self.password,
            "balance": self.balance,
            "account_type": self.account_type,
            "transactions": self.get_transaction_list(),
            "loan_balance": self.loan_balance,
            "annual_interest_rate": self.annual_interest_rate
        }
