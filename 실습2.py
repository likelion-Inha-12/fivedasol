class Account:
    def __init__(self):
        self.money = 0
    
    def add(self, money):
        if money<0:
            print("금액은 양수여야 합니다.")
        else:
            self.money += money
            print("%d원 입금되었습니다." %money)
    
    def sub(self, money):
        if money<0:
           print("금액은 양수여야 합니다.")
        elif money > self.money:
            print("출금 금액이 잔액을 초과했습니다.")
        else:
            self.money -= money
            print("%d원이 출금되었습니다." %money)

    def check(self):
        print("dasol님의 계좌 잔액은 %d원입니다." %self.money)


# dasol = Account()
# dasol.check()
# dasol.add(10000)
# dasol.sub(20000)
# dasol.sub(5000)
# dasol.check()
# dasol.add(-100)
# dasol.add(12000)
# dasol.check()