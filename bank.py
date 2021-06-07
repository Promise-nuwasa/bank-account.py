from datetime import datetime
class Account:
    def __init__(self,name,phone_number):
        self.name=name
        self.phone_number=phone_number
        self.balance=0
        self.loan=0
        self.statement=[]
    def show_balance(self):
        return f"hello your balance is UGSH{self.balance}"

    def deposit(self,amount):
        if amount<0:
            return
        else:   
            self.balance+=amount   
            now=datetime.now()

            transaction={
            "amount":amount,
            "time":now,
            "narration":"you have deposited"
             }
            self.statement.append(transaction)
            return self.show_balance()

    def show_statement(self):
            for transaction in self.statement:
                amount=transaction["amount"]
                narration=transaction["narration"]
                time=transaction["time"]
                date=time.strftime("%d/%m/%y")
                print(f"{date} : {narration} {amount}")
     
            return (f"Hello you deposited {amount} on {date}")

    def withdraw(self,amount):
        if amount>self.balance:
            transaction={
            "amount":amount,
            "time":now,
            "narration":"you have deposited"
             }
            self.statement.append(transaction)

            return f"your balance is {self.balance} and you can not withdraw {amount}"
        else:
            self.balance-=amount
            return self.show_balance()

    def update(self,amount):
        if amount<self.balance:
            return f"You have updated  {self.balance} and your balance is {amount}" 
        else:
            self.balance+=amount
            return  self.show_balance()    
         
    def borrow(self,amount):
        if amount < 0:
            return f"You can not get a loan because your amount is low"
        elif self.loan >0:
            return f"You have an out standing loan of UGsh{amount}"
        elif amount<0.1*self.balance:
            return f"you are not qualified for a loan"
        else:
            loan=amount*1.05
            now=datetime.now()
            transaction={
            "amount":amount,
            "time":now,
            "narration":"you have deposited"}
            self.statement.append(transaction)
            self.loan=loan
            self.balance+=amount
            return f"You qualify for a loan of UGsh{self.loan}"

            

    def repay(self,amount):
        if amount <0:
            return f"you loan balance is 0 so "
        elif amount<=self.loan:
            self.loan-=amount
            return f"you have repaid  your loan and your balance is UGsh{self.loan}"
        else:
             diff=amount - self.loan
             self.loan=0
             now=datetime.now()
             transaction={
            "amount":amount,
            "time":now,
            "narration":"you have deposited"}
             self.statement.append(transaction)

             self.deposit(amount-loan)
             return f"Hello you have repaid your loan  and your balance is UGsh{self.deposit}"
           
          




