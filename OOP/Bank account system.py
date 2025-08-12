class bank_account_details:

    def account_info(self): # This is used for checking bank info.
        print(f"\nName: {self.account_holder_name}")
        print(f"A/c no: {self.account_number}")
        print(f"A/c type: {self.account_type}\n")
        # print(f"Transaction type: {self.amount_withdrawn}") # Created this for future expansion.

    def __init__(self, name = "default"): # This have effect in the above account_info function

        self.account_holder_name = name
        self.account_type = "Savings"
        self.account_number = 83659196501
        self.amount_withdrawn = 500
        self.amount_deposited = 0

balances = {    # Banks maintain a data base so I created a small dictionary to maintain mine.
    "naman": 248000,
    "jake": 46000,
    "simon": 360000,
    "rohit": 24000
}

def user_identity(user_name): # This helps in identifying the name and the amount in dictionary.

    if user_name in balances:
        return balances[user_name]

    else:
        print("\nSorry, your details are not present in our data system.\n")
        return None

user_name = input("\nPlease enter your name: ").lower()
user = bank_account_details(user_name)

# user.account_info()

print(f'''\nHello, {user.account_holder_name}\nWelcome to the banking menu\n
1. Check Balance.\n2. Withdraw Money\n3. Deposit Money\n4. Check Bank Info''')

goal = ["check balance", "withdraw money", "deposit money", "check bank info"]

user_goal = input("\nWhat would you like to do?\n")

def show_balance():
    if user_goal == goal[0]:
        amount = user_identity(user_name)
        print(f"\nYour bank balance is: {amount}\n")

    elif user_goal == goal[1]:

        amount = int(input(f"\nEnter the amount you want to withdraw from the bank: "))

        if (amount <= balances[user_name]):

            remaining_balance = balances[user_name] - amount
            print(f"\nWithdrawl successful, your remaining balance is: {remaining_balance}\n")

        else:
            print("\nPlease enter a valid amount.\n")

    elif user_goal == goal[2]:

        amount = int(input(f"\nEnter the amount you want to deposit in the bank: "))

        new_balance = balances[user_name] + amount

        # balances[user_name] = new_balance

        print(f"\nDeposit successful, your new balance is: {new_balance}\n")

    elif user_goal == goal[3]:

        user = bank_account_details(user_name)
        user.account_info()

    else:
        print("\nSorry, balance not available.\n")

show_balance()