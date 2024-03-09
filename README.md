US overseas tax tools
========================

US overseas citizens have to file US taxes, which is obviously super fun and enjoyable.

Part of this includes reporting the interest earned in all your bank accounts, in the calendar year.
Because Australia's tax year runs from mid year to mid year (eg july 2022 - june 2023), and so Australian banks will only make nice interest summaries for that year.

These are just quick scripts I wrote for myself (/had ChatGPT write for me mostly), its probably just as fast to do it in Excel (except for Up). Use at your own risk, do not sue me if somehow you get in trouble for issues with your taxes (or any other kind of issues - MIT license / make no warranties etc.), I'm mostly just saving these here so I can easily find them again next year.

# How to use (per bank):

## Westpac
1. Sign in online
2. Go to Overview > Exports and reports > Transactiosn > Export CSV
3. Set the date range to the relevant calendar year
4. Select all accounts
5. Download as csv
6. run `python3 westpac_to_accounts.py /path/to/export.csv`

## Macquarie
1. Sign in online
2. Click on an account
3. Click the download button (to the left of the printer, just above the large list of transactions)
4. run `python3 macquarie_interest_to_accounts.py /path/to/account_transactions.csv`
5. Repeat for each account you have with macquarie

## Up bank
Up sadly does not have an easy way to export all your transactions as a CSV (you can export them for each month, from your phone, and then email them to your computer... but no way to get a whole calendar year... 😢)

Luckily they have an API you can use to get all your transactions.
Steps:
1. Go to https://developer.up.com.au/#welcome
2. Get a personal access token
3. Store that access token in 'UP_AUTH_TOKEN'
4. run `python3 up_download_transactions.py` which will generate `up_transactions.csv`
5. run `python3 up_interest_summariser.py up_transactions.csv` 
Even though you can have multiple 'savers' with Up as these don't get different BSB / account numbers I think these all just count as one account anyway - the script also makes that assumption and will just return the total interest earned from Up.
