import os
from handlers.transaction_handler import TransactionHandler

print('file path:', os.path.join(os.path.dirname(__file__), 'files/transactions.csv'))

transaction_handler = TransactionHandler(os.path.join(os.path.dirname(__file__), 'files/transactions.csv'))
transaction_handler.run()
