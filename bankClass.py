
class Bank:

    """
    This bank class has methods such as Deposit() and withrawal()
    """

    def __init__(self):
        self._bankName= "Chase"
        self.amount= 0.00


    def __str__(self):

        return f"Welcome to {self._bankName}!. \n Current balance is {self.amount} \n Make deposit Now"



    def Deposit(self):
        amount= float(input("Enter deposit amount: "))
        self.amount= self.amount + amount 

        return f"You deposited USD {self.amount}"


    def Withrawal(self):

        amount= float(input("How much do you want to withdraw? : "))
            
        while True:
            
            amount= float(input(f"Withdraw a lower amount your balance now = USD{self.amount}: "))
            
            if (amount > self.amount):
                
                print(f"cant withraw this amount.Your current balance = USD{self.amount}")
                
                continue
                
            else:
                
                self.amount= self.amount - amount
                
                return f"You withdrawn USD{amount} your current balance= USD{self.amount}"


    def CheckBalance(self):

        return f" Your current balance = USD{self.amount}"


        



    


        
            
            
            

