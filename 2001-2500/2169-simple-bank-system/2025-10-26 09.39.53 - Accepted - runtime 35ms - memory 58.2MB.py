class Bank:

    def __init__(self, balance: List[int]):
        self.n=balance
        self.L=set(range(1, len(balance)+1))

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 in self.L and account2 in self.L:
            if self.n[account1-1]>=money:
                self.n[account1-1]-=money
                self.n[account2-1]+=money
                return True
            else:
                return False
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if account in self.L:
            self.n[account-1]+=money
            return True
        else:
            return False

    def withdraw(self, account: int, money: int) -> bool:
        if account in self.L:
            if self.n[account-1]>=money:
                self.n[account-1]-=money
                return True
            else:
                return False
        else:
            return False

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)