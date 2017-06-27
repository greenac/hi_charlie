import os
from handlers.transaction_handler import TransactionHandler

if os.environ['HICHARLIE_TRANSACTIONS_PATH']:
    print('file path:', os.environ['HICHARLIE_TRANSACTIONS_PATH'])
    transaction_handler = TransactionHandler(os.environ['HICHARLIE_TRANSACTIONS_PATH'])
    transaction_handler.run()
else:
    print(
        'Error: sorry you must set the path to the transactions.csv',
        'file as (HICHARLIE_TRANSACTIONS_PATH) in your environment.'
    )
