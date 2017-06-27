from models.transaction import Transaction
from errors.errors import TransactionParseException
import sys


class CSVHandler:
    def __init__(self, file_path):
        self._file_path = file_path

    def parse(self):
        return self._read_transactions()

    def _read_transactions(self):
        transactions = []
        try:
            with open(self._file_path, encoding='latin-1') as read_file:
                for index, line in enumerate(read_file):
                    if index == 0:
                        continue
                    try:
                        transaction = self._parse_line(line)
                    except TransactionParseException:
                        print('transaction parse exception occured')
                        continue
                    except:
                        print('Hit random exception parsing transaction:', sys.exc_info()[0])
                        continue
                    transactions.append(transaction)
            read_file.close()
        except UnicodeDecodeError:
            print('Error: could not decode unicode. Error:', sys.exc_info()[0])
        except:
            print('Error: opening file:', self._file_path, 'error:', sys.exc_info()[0])
            raise
        return transactions

    def _parse_line(self, line):
        parts = line.split(',')
        try:
            account_types = parts[3].lower().replace('(', '').replace(')', '').split(' ')
            account_type = account_types[0]
            del account_types[0]
            if len(account_types) > 1:
                payment_method = '_'.join(account_types)
            else:
                payment_method = account_types[0]

            transaction = Transaction(
                user_id=int(parts[0]),
                account_id=int(parts[1]),
                account_institution=parts[2].lower(),
                account_type=account_type,
                payment_method=payment_method,
                amount=float(parts[4]),
                year=int(parts[5]),
                month=int(parts[6]),
                day=int(parts[7]),
                day_of_week=int(parts[8]),
                name=parts[9].lower()
            )
        except IndexError:
            print('Error: could not parse transaction:', parts)
            raise TransactionParseException('Failed to parse line: ' + line)
        return transaction



