import json

# --------------------------------------------------
# FUNCTION 1: Read ledger and build account -> amounts
# --------------------------------------------------
def read_ledger(file_path):
    """
    Reads transaction ledger line by line.
    Returns:
    account_id -> list of transaction amounts
    """
    account_data = {}

    with open(file_path, "r") as file:
        for line in file:
            # Skip empty lines
            if not line.strip():
                continue

            parts = line.split(",")

            transaction_id = parts[0].strip()
            account_id = parts[1].strip()
            amount = int(parts[2].strip())

            # Initialize list if account not seen
            if account_id not in account_data:
                account_data[account_id] = []

            # Append transaction amount
            account_data[account_id].append(amount)

    return account_data


# --------------------------------------------------
# FUNCTION 2: Compute ledger consistency per account
# --------------------------------------------------
def compute_summary(account_data):
    """
    Computes:
    final_balance
    ever_negative
    transaction_count
    """
    summary = {}

    for account in account_data:
        amounts = account_data[account]

        balance = 0
        ever_negative = False

        for amt in amounts:
            balance = balance + amt
            if balance < 0:
                ever_negative = True

        summary[account] = {
            "final_balance": balance,
            "ever_negative": ever_negative,
            "transaction_count": len(amounts)
        }

    return summary


# --------------------------------------------------
# FUNCTION 3: Write summary to JSON
# --------------------------------------------------
def write_json(summary, output_file):
    """
    Writes summary dictionary to JSON file
    """
    with open(output_file, "w") as f:
        json.dump(summary, f, indent=4)


# --------------------------------------------------
# MAIN PROGRAM (EXAM FRIENDLY)
# --------------------------------------------------
ledger_file = "ledger.txt"          # input file
output_file = "ledger_summary.json" # output JSON

account_data = read_ledger(ledger_file)
summary = compute_summary(account_data)
write_json(summary, output_file)

# Optional print for checking
for acc in summary:
    print(acc, "->", summary[acc])
