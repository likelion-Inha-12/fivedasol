from 실습2 import Account

class Bank(Account):
    def __init__(self):
        self.money=0

    def add(self, money, plus):
        if money<0:
            print("금액은 양수여야 합니다.")
        else:
            self.check()
            self.money += money
            print("이자율: %d" %plus)
            print("%d원 입금되었습니다." %money)
            add_money = (self.money)*(plus/100)
            self.money+= add_money
            print("dasol님의 계좌에 %d원의 이자가 추가되었습니다."%add_money)


# dasol=Bank()
# dasol.check()
# dasol.add(1500,5)
# dasol.sub(100)