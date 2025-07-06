class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def __str__(self):
        # 🔽 Sort accounts by name using __lt__ defined in SavingsAccount
        sorted_accounts = sorted(self.accounts)
        return '\n'.join(str(account) for account in sorted_accounts)
