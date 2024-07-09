#this is a file for one class called TableRecord

class TableRecord():
    def __init__(self, nr, quanity, unit_price, gotten_money, payment_type, date) -> None:
        self.nr = nr 
        self.quanity = quanity
        self.unit_price = unit_price
        self.gotten_money = gotten_money  #It's named like that so as not to confuse with "income"
        self.payment_type = payment_type
        self.date = date

        #it will load data using "shelves" module
        #and then in a loop creating object of this class
        #and those will be saved in a dictionary like this
        # self.user_list[account_number] = UserWidget(self,self.scrollable_frame,name,account_number)
        # i can also make it so it counts money automatically