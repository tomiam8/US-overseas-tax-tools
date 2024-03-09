import csv
import sys

# Constant for the year to filter the transactions
FOR_YEAR = '2023'
file_path = sys.argv[1]  # Replace this with your actual file path or keep as is to use command line argument

# Function to calculate the sum of 'Interest' amounts
def calculate_interest_sum(file_path, for_year):
    total_interest_cents = 0  # Variable to hold the sum of interest amounts in cents

    # Open the file and read the data
    with open(file_path, newline='') as csvfile:
        data_reader = csv.DictReader(csvfile)  # Assuming the file is comma-delimited
        for row in data_reader:
            # Check if the transaction is for 'Interest' and within the specified year
            transaction_year = row['Created Time'][:4]  # Extract the year part from the 'Created Time'
            if transaction_year == for_year and row['Description'] == 'Interest':
                # Process amount value as cents
                amount_cents = int(float(row['Amount Value']) * 100)  # Convert the amount to cents
                total_interest_cents += amount_cents

    # Convert the total from cents to dollars for printing
    dollars, cents = divmod(total_interest_cents, 100)
    print(f"Total 'Interest' amount for {for_year}: ${dollars}.{cents:02d}")

calculate_interest_sum(file_path, FOR_YEAR)

