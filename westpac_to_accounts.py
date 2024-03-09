import csv
import sys

# Path to your CSV file
file_path = sys.argv[1]

# Initialize a dictionary to hold the sum of credit amounts for each account
credit_sums = {}

# Open the file and read the data
with open(file_path, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)  # Using DictReader to access columns by names
    for row in data_reader:
        # Check if the category is 'INT' and credit amount is not empty
        if row['Categories'] == 'INT' and row['Credit Amount']:
            # Split the credit amount into dollars and cents
            dollars, cents = row['Credit Amount'].split('.')
            total_cents = int(dollars) * 100 + int(cents)

            # Get the account number from the row
            account = row['Bank Account']

            # If the account is already in the dictionary, add to its total
            if account in credit_sums:
                credit_sums[account] += total_cents
            else:
                # Otherwise, initialize the account's total with the current amount
                credit_sums[account] = total_cents

# Print the sum of credit amounts in dollars and cents for each account
for account, total_cents in credit_sums.items():
    dollars, cents = divmod(total_cents, 100)
    print(f"Account {account}: Total Credit Amount: ${dollars}.{cents:02d}")

