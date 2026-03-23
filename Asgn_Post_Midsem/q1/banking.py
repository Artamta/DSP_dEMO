#!/usr/bin/python3

# 1. Identifylocations where exceptions may occur.
# 2. Modify the program to handle exception identified in step (1).
# 3. Ensure the program continues execution even after errors.
# 4. Implement at least one custom exception.

# 5. Develop test cases for thoroughly testing all operations.

def load_accounts(filename):
    accounts = {}
        file = open(filename, "r")

    for line in file:
        parts = line.strip().split(",")
        acc_no = parts[0]
        name = parts[1]
        balance = float(parts[2])

        accounts[acc_no] = {
            "name": name,
            "balance": balance,
            "transactions": []
        }

    file.close()
    return accounts

def save_accounts(filename, accounts):
    file = open(filename, "w")

    for acc in accounts:
        acc_data = accounts[acc]
        line = acc + "," + acc_data["name"] + "," + str(acc_data["balance"])
        file.write(line + "\n")

    file.close()

def create_account(accounts):
    acc_no = input("Enter account number: ")
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial deposit: "))

    accounts[acc_no] = {
        "name": name,
        "balance": balance,
        "transactions": []
    }

    print("Account created")

def deposit(accounts):
    acc_no = input("Enter account number: ")
    amount = float(input("Enter amount to deposit: "))
    account = accounts[acc_no]
    account["balance"] += amount
    account["transactions"].append(("deposit", amount))
    print("Deposit successful")

def withdraw(accounts):
    acc_no = input("Enter account number: ")
    amount = float(input("Enter withdrawal amount: "))
    account = accounts[acc_no]
    if account["balance"] >= amount:
        account["balance"] -= amount
        account["transactions"].append(("withdraw", amount))
        print("Withdrawal successful")
    else:
        print("Insufficient balance")

def transfer(accounts):
    source = input("Enter source account: ")
    target = input("Enter target account: ")
    amount = float(input("Enter amount: "))

    src_acc = accounts[source]
    tgt_acc = accounts[target]

    if src_acc["balance"] >= amount:
        src_acc["balance"] -= amount
        tgt_acc["balance"] += amount
        src_acc["transactions"].append(("transfer_out", amount))
        tgt_acc["transactions"].append(("transfer_in", amount))
        print("Transfer successful")
    else:
        print("Insufficient funds")

def display_account(accounts):
    acc_no = input("Enter account number: ")
    account = accounts[acc_no]

    print("Account number:", acc_no)
    print("Name:", account["name"])
    print("Balance:", account["balance"])

def transaction_history(accounts):
    acc_no = input("Enter account number: ")
    account = accounts[acc_no]

    print("Transaction history")
    for t in account["transactions"]:
        print(t[0], t[1])

def apply_interest(accounts):
    rate = float(input("Enter interest rate (%): "))

    for acc in accounts:
        account = accounts[acc]
        interest = account["balance"] * rate / 100
        account["balance"] += interest

    print("Interest applied to all accounts")

def richest_account(accounts):
    max_balance = -1
    richest = None

    for acc in accounts:
        bal = accounts[acc]["balance"]

        if bal > max_balance:
            max_balance = bal
            richest = acc

    print("Richest account:", richest)
    print("Balance:", max_balance)

def total_bank_balance(accounts):
    total = 0
    for acc in accounts:
        total += accounts[acc]["balance"]

    print("Total bank balance:", total)

def remove_account(accounts):
    acc_no = input("Enter account number to delete: ")
    del accounts[acc_no]
    print("Account deleted")

def menu():
    print()
    print("Bank Management System")
    print("----------------------")
    print("1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Display account")
    print("6. Transaction history")
    print("7. Apply interest")
    print("8. Richest account")
    print("9. Total bank balance")
    print("10. Remove account")
    print("11. Save data")
    print("12. Exit")

def main():
    filename = input("Enter account file: ")
    accounts = load_accounts(filename)

    while True:
        menu()
        choice = int(input("Enter choice: "))
        if choice == 1:
            create_account(accounts)

        elif choice == 2:
            deposit(accounts)

        elif choice == 3:
            withdraw(accounts)

        elif choice == 4:
            transfer(accounts)

        elif choice == 5:
            display_account(accounts)

        elif choice == 6:
            transaction_history(accounts)

        elif choice == 7:
            apply_interest(accounts)

        elif choice == 8:
            richest_account(accounts)

        elif choice == 9:
            total_bank_balance(accounts)

        elif choice == 10:
            remove_account(accounts)

        elif choice == 11:
            save_accounts(filename, accounts)

        elif choice == 12:
            break

        else:
            print("Invalid choice")


main()
