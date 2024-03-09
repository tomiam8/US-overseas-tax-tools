import csv
from urllib.parse import urlencode, parse_qsl
import requests

def get_auth_token(filename):
    """Reads the authentication token from a file."""
    with open(filename, 'r') as file:
        return file.readline().strip()

def fetch_transactions(url, headers):
    """Fetches all transactions from the API, following pagination."""
    all_transactions = []
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            all_transactions.extend(data['data'])
            print(f"Fetched {len(data['data'])} transactions.")
            url = data['links'].get('next')
            if url:
                # Correctly handle the URL for the next page
                url = f"{url.split('?', 1)[0]}?{urlencode(parse_qsl(url.split('?', 1)[1]), safe=':', quote_via=requests.utils.quote)}"
        else:
            print(f"Failed to retrieve data: {response.status_code}, details: {response.json()}")
            break
    return all_transactions

def write_to_csv(transactions, csv_file):
    """Writes the transactions to a CSV file."""
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Description', 'Message', 'Amount Value', 'Amount Currency', 'Created Time', 'Category'])
        for transaction in transactions:
            attributes = transaction['attributes']
            category = f"{transaction['relationships']['category']['data']['type']}:{transaction['relationships']['category']['data']['id']}" \
                if transaction['relationships']['category']['data'] else 'N/A'
            writer.writerow([
                transaction['id'],
                attributes['description'],
                attributes['message'],
                attributes['amount']['value'],
                attributes['amount']['currencyCode'],
                attributes['createdAt'],
                category
            ])
    print(f"Data written to {csv_file}")

auth_token = get_auth_token('UP_AUTH_TOKEN')
headers = {'Authorization': f'Bearer {auth_token}'}
base_url = 'https://api.up.com.au/api/v1/transactions'
params = {
    'filter[since]': '2023-01-01T00:00:00+00:00',
    'filter[until]': '2023-12-31T23:59:59+00:00',
    'page[size]': 50
}
encoded_params = urlencode(params, safe=':', quote_via=requests.utils.quote)
url = f"{base_url}?{encoded_params}"
print(f"Fetching data from {url}...")
transactions = fetch_transactions(url, headers)
if transactions:
    write_to_csv(transactions, 'up_transactions.csv')
else:
    print("No transactions fetched.")
