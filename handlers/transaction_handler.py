from handlers.csv_handler import CSVHandler
from utils.transaction_printer import format_transaction


class TransactionHandler:
    def __init__(self, file_path):
        self._file_path = file_path
        self._transactions = []
        self._mortgages = []

    def run(self):
        self._fill_transactions()
        self._fill_mortgages()
        print('Found', len(self._mortgages), 'mortgages')
        user_mortgages = self._mortgages_for_user()
        for user_id, transactions in user_mortgages.items():
            print('Mortgage payments for user:', user_id)
            for index, transaction in enumerate(transactions):
                print(index, ':', format_transaction(transaction))
        return None

    # def check_periodicity(self):
    #     periodic_transactions
    def _fill_transactions(self):
        csv_handler = CSVHandler(self._file_path)
        self._transactions = csv_handler.parse()
        return None

    def _is_mortgage(self, transaction):
        return (('mortgage' in transaction.name or 'rent' in transaction.name) and
                transaction.account_type == 'depository'and
                transaction.amount > 125.0)

    def _fill_mortgages(self):
        self._mortgages = [transaction for transaction in self._transactions if self._is_mortgage(transaction)]
        return None

    def _mortgages_for_user(self):
        user_mortgages = {}
        for transaction in self._mortgages:
            if transaction.user_id in user_mortgages:
                user_mortgages[transaction.user_id].append(transaction)
            else:
                user_mortgages[transaction.user_id] = [transaction]
        return user_mortgages
