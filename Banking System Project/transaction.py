# transaction.py
from datetime import datetime

class TransactionNode:
    def __init__(self, transaction_id, amount, transaction_type):
        self.transaction_id = transaction_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.next = None

    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "amount": self.amount,
            "transaction_type": self.transaction_type,
            "timestamp": self.timestamp
        }
