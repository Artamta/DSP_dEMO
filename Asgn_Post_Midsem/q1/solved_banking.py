#!/usr/bin/python3

# Custom Exception
class InsufficientBalanceError(Exception):
    pass


# Load accounts
def load_accounts(filename):
    accounts = {}
    try:
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

    except FileNotFoundError:
        print("File not found. Starting with empty database.")

    except ValueError:
        print("Error in file format.")

    return accounts


# Save accounts
def save_accounts(filename, accounts):
    try:
        file = open(filename, "w")

        for acc in accounts:
            acc_data = accounts[acc]
            line = acc + "," + acc_data["name"] + "," + str(acc_data["balance"])
            file.write(line + "\n")

        file.close()
        print("Data saved successfully")

    except IOError:
        print("Error writing to file")


# Create account
def create_account(accounts):
    try:
        acc_no = input("Enter account number: ")

        if acc_no in accounts:
            print("Account already exists")
            return

        name = input("Enter account holder name: ")
        balance = float(input("Enter initial deposit: "))

        accounts[acc_no] = {
            "name": name,
            "balance": balance,
            "transactions": []
        }

        print("Account created")

    except ValueError:
        print("Invalid input")


# Deposit
def deposit(accounts):
    try:
        acc_no = input("Enter account number: ")
        amount = float(input("Enter amount: "))

        account = accounts[acc_no]
        account["balance"] += amount
        account["transactions"].append(("deposit", amount))

        print("Deposit successful")

    except KeyError:
        print("Account not found")
    except ValueError:
        print("Invalid amount")


# Withdraw
def withdraw(accounts):
    try:
        acc_no = input("Enter account number: ")
        amount = float(input("Enter amount: "))

        account = accounts[acc_no]

        if account["balance"] < amount:
            raise InsufficientBalanceError("Insufficient balance")

        account["balance"] -= amount
        account["transactions"].append(("withdraw", amount))

        print("Withdrawal successful")

    except KeyError:
        print("Account not found")
    except ValueError:
        print("Invalid amount")
    except InsufficientBalanceError as e:
        print(e)


# Transfer
def transfer(accounts):
    try:
        source = input("Enter source account: ")
        target = input("Enter target account: ")
        amount = float(input("Enter amount: "))

        src_acc = accounts[source]
        tgt_acc = accounts[target]

        if src_acc["balance"] < amount:
            raise InsufficientBalanceError("Insufficient funds")

        src_acc["balance"] -= amount
        tgt_acc["balance"] += amount

        src_acc["transactions"].append(("transfer_out", amount))
        tgt_acc["transactions"].append(("transfer_in", amount))

        print("Transfer successful")

    except KeyError:
        print("Invalid account number")
    except ValueError:
        print("Invalid amount")
    except InsufficientBalanceError as e:
        print(e)


# Display account
def display_account(accounts):
    try:
        acc_no = input("Enter account number: ")
        account = accounts[acc_no]

        print("Account number:", acc_no)
        print("Name:", account["name"])
        print("Balance:", account["balance"])

    except KeyError:
        print("Account not found")


# Transaction history
def transaction_history(accounts):
    try:
        acc_no = input("Enter account number: ")
        account = accounts[acc_no]

        print("Transaction history:")
        for t in account["transactions"]:
            print(t[0], t[1])

    except KeyError:
        print("Account not found")


# Apply interest
def apply_interest(accounts):
    try:
        rate = float(input("Enter interest rate (%): "))

        for acc in accounts:
            interest = accounts[acc]["balance"] * rate / 100
            accounts[acc]["balance"] += interest

        print("Interest applied")

    except ValueError:
        print("Invalid rate")


# Richest account
def richest_account(accounts):
    try:
        max_balance = -1
        richest = None

        for acc in accounts:
            bal = accounts[acc]["balance"]

            if bal > max_balance:
                max_balance = bal
                richest = acc

        print("Richest account:", richest)
        print("Balance:", max_balance)

    except Exception:
        print("Error finding richest account")


# Total bank balance
def total_bank_balance(accounts):
    total = 0
    for acc in accounts:
        total += accounts[acc]["balance"]

    print("Total bank balance:", total)


# Remove account
def remove_account(accounts):
    try:
        acc_no = input("Enter account number: ")
        del accounts[acc_no]

        print("Account deleted")

    except KeyError:
        print("Account not found")


# Menu
def menu():
    print("\nBank Management System")
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


# Main
def main():
    filename = input("Enter account file: ")
    accounts = load_accounts(filename)

    while True:
        try:
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
                print("Exiting...")
                break
            else:
                print("Invalid choice")

        except ValueError:
            print("Enter a valid number")
        except Exception as e:
            print("Unexpected error:", e)


main()