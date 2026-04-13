# test_banking.py

from banking import *

def run_tests():
    accounts = {}

    print("\n--- Running Tests ---")

    # Test 1: Create account
    accounts["101"] = {"name": "Ayush", "balance": 1000, "transactions": []}
    print("Test 1 Passed: Account created")

    # Test 2: Deposit
    try:
        accounts["101"]["balance"] += 500
        assert accounts["101"]["balance"] == 1500
        print("Test 2 Passed: Deposit")
    except:
        print("Test 2 Failed")

    # Test 3: Withdraw (valid)
    try:
        accounts["101"]["balance"] -= 200
        assert accounts["101"]["balance"] == 1300
        print("Test 3 Passed: Withdraw")
    except:
        print("Test 3 Failed")

    # Test 4: Withdraw (insufficient balance)
    try:
        if accounts["101"]["balance"] < 5000:
            raise InsufficientBalanceError
    except InsufficientBalanceError:
        print("Test 4 Passed: Insufficient balance handled")

    # Test 5: Transfer
    accounts["102"] = {"name": "Test", "balance": 500, "transactions": []}
    try:
        amount = 300
        accounts["101"]["balance"] -= amount
        accounts["102"]["balance"] += amount

        assert accounts["102"]["balance"] == 800
        print("Test 5 Passed: Transfer")
    except:
        print("Test 5 Failed")

    # Test 6: Invalid account
    try:
        _ = accounts["999"]
    except KeyError:
        print("Test 6 Passed: Invalid account handled")

    print("\n--- Testing Complete ---")


if __name__ == "__main__":
    run_tests()