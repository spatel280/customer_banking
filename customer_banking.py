# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Enter your savings balance: "))
    savings_interest_rate = float(input("Enter your interest rate: "))
    savings_months = int(input("Enter your number of months: "))

    # Call the create_savings_account function and pass the variables from the user.
    # updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    new_savings_account = create_savings_account(savings_balance, savings_interest_rate, savings_months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Your new savings account has a starting balance of ${new_savings_account['savings_balance']} and interest earned of ${new_savings_account['savings_interest_earned']}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE

if __name__ == "__main__":
    main()
