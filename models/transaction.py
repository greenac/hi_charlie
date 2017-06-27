from datetime import date


class Transaction:
    def __init__(
            self,
            user_id,
            account_id,
            account_institution,
            account_type,
            payment_method,
            amount,
            year,
            month,
            day,
            day_of_week,
            name
    ):
        self.user_id = user_id
        self.account_id = account_id
        self.account_institution = account_institution
        self.account_type = account_type
        self.payment_method = payment_method
        self.amount = amount
        self.year = year
        self.month = month
        self.day = day
        self.day_of_week = day_of_week
        self.name = name

    def __str__(self):
        return 'user_id: {}, account_id: {}, account_institution: {}, account_type: {}, payment_method: {}, amount: {}, date: {}, name: {}'.format(
            self.user_id,
            self.account_id,
            self.account_institution,
            self.account_type,
            self.payment_method,
            self.amount,
            self.get_date(),
            self.name
        )

    def get_date(self):
        return date(self.year, self.month, self.day)

    def key(self):
        return '{}_{}_{}_{}_{}'.format(self.user_id, self.account_type, self.account_id, self.amount, self.get_date())