import csv
import sys

# Constant for the year to filter the transactions
FOR_YEAR = '2023'
file_path = sys.argv[1]

# Function to calculate the sum of credits minus debits for 'Interest' subcategory in cents
def calculate_interest_sum(file_path, for_year):
    interest_sums = {}  # Dictionary to hold the sum of credits minus debits in cents for each account

    # Open the file and read the data
    with open(file_path, newline='') as csvfile:
        data_reader = csv.DictReader(csvfile, delimiter=',')  # Assuming the file is comma-delimited
        for row in data_reader:
            # Extract year from the 'Transaction Date' and check if it matches FOR_YEAR
            transaction_year = row['Transaction Date'].split(' ')[-1]
            if transaction_year == for_year and row['Subcategory'] == 'Interest':
                # Process credit amount
                credit_dollars, credit_cents = (0, 0)
                if row['Credit']:
                    parts = row['Credit'].split('.')
                    credit_dollars = int(parts[0]) * 100
                    credit_cents = int(parts[1]) if len(parts) > 1 else 0

                # Process debit amount
                debit_dollars, debit_cents = (0, 0)
                if row['Debit']:
                    parts = row['Debit'].split('.')
                    debit_dollars = int(parts[0]) * 100
                    debit_cents = int(parts[1]) if len(parts) > 1 else 0

                # Calculate net credit in cents
                net_credits = credit_dollars + credit_cents - debit_dollars - debit_cents

                # Add to the account's total in the dictionary
                account = row['Account']
                if account in interest_sums:
                    interest_sums[account] += net_credits
                else:
                    interest_sums[account] = net_credits

    # Convert the totals to dollars and cents for printing
    for account, total_cents in interest_sums.items():
        dollars, cents = divmod(total_cents, 100)
        # Print out the formatted total for each account
        print(f"Account {account}: Total 'Interest' net amount for {for_year}: ${dollars}.{cents:02d}")

calculate_interest_sum(file_path, FOR_YEAR)

