class Bank:

    def __init__(self, balance: List[int]):
        self.d=balance
        self.r=range(1, len(balance)+1)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 in self.r and account2 in self.r:
            if self.d[account1-1]>=money:
                self.d[account1-1]-=money
                self.d[account2-1]+=money
                return True
            
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account in self.r:
            self.d[account-1]+=money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if account in self.r:
            if self.d[account-1]>=money:
                self.d[account-1]-=money
                return True

        return False

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)