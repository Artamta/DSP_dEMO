import json

# 1. Setup storage
# account_history will look like: {'acc1': [100, -40, -60], 'acc2': [200]}
account_history = {}

# 2. Read and Build Data Structure
with open("sample/ledger.txt", "r") as f:
    for line in f:
        if line.startswith('t'):  # Simplest way to skip junk/empty lines
            parts = line.strip().split(",")
            acc_id = parts[1].strip()
            amount = float(parts[2].strip())
            
            # If account isn't in dictionary yet, create a list for it
            if acc_id not in account_history:
                account_history[acc_id] = []
            
            # Add the amount to that account's list
            account_history[acc_id].append(amount)

# 3. Compute Stats & Create Summary Dictionary
summary = {}

for acc_id, transactions in account_history.items():
    # Final Balance logic
    balance = sum(transactions)
    
    # "Ever Negative" logic (check balance step-by-step)
    running_total = 0
    was_negative = False
    for t in transactions:
        running_total += t
        if running_total < 0:
            was_negative = True
            break # We found it, no need to keep checking
            
    # Store in the required format
    summary[acc_id] = {
        "final_balance": balance,
        "ever_negative": was_negative,
        "transaction_count": len(transactions)
    }

# 4. Write to JSON
with open("summary.json", "w") as out_f:
    json.dump(summary, out_f, indent=4)

print("Summary created successfully!")
