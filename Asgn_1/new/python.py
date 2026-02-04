# ====================== PYTHON MASTER EXAM CHEATSHEET ======================
# Purpose:
# - Beginner friendly
# - All common Python logics in one file
# - Copy-paste and modify during exam
# - Covers lists, strings, files, dictionaries, stats, CSV, JSON

# ========================================================================
# BASIC PRINTING & VARIABLES
# ========================================================================

print("Hello Python")

a = 10
b = 20
print("Sum:", a + b)

# ========================================================================
# LIST UTILITIES
# ========================================================================

def print_list(lst):
    for x in lst:
        print(x)


def sum_list(lst):
    total = 0
    for x in lst:
        total = total + x
    return total


def count_list(lst):
    count = 0
    for _ in lst:
        count = count + 1
    return count


def mean_list(lst):
    total = 0
    count = 0
    for x in lst:
        total = total + x
        count = count + 1
    return total / count


def min_list(lst):
    minimum = lst[0]
    for x in lst:
        if x < minimum:
            minimum = x
    return minimum


def max_list(lst):
    maximum = lst[0]
    for x in lst:
        if x > maximum:
            maximum = x
    return maximum


def count_even_odd(lst):
    even = 0
    odd = 0
    for x in lst:
        if x % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    return even, odd


def separate_positive_negative(lst):
    positive = []
    negative = []
    for x in lst:
        if x >= 0:
            positive.append(x)
        else:
            negative.append(x)
    return positive, negative


def unique_list(lst):
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result


def frequency_list(lst):
    freq = {}
    for x in lst:
        if x not in freq:
            freq[x] = 0
        freq[x] = freq[x] + 1
    return freq

# ========================================================================
# STRING UTILITIES
# ========================================================================

def count_words(text):
    words = text.split()
    return len(words)


def string_to_upper(text):
    return text.upper()


def string_to_lower(text):
    return text.lower()

# ========================================================================
# FILE HANDLING (TEXT FILES)
# ========================================================================

def read_file(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line.strip())


def count_lines(filename):
    count = 0
    with open(filename, "r") as f:
        for _ in f:
            count = count + 1
    return count


def read_numbers_from_file(filename):
    numbers = []
    with open(filename, "r") as f:
        for line in f:
            numbers.append(int(line.strip()))
    return numbers


def mean_from_file(filename):
    nums = read_numbers_from_file(filename)
    return mean_list(nums)

# ========================================================================
# DICTIONARY UTILITIES (VERY IMPORTANT)
# ========================================================================

def print_dict(d):
    for key in d:
        print(key, ":", d[key])


def frequency_from_file(filename):
    freq = {}
    with open(filename, "r") as f:
        for line in f:
            word = line.strip()
            if word not in freq:
                freq[word] = 0
            freq[word] = freq[word] + 1
    return freq

# ========================================================================
# LOG FILE STYLE PROCESSING
# Format: timestamp, user, event
# ========================================================================

def read_log_file(filename):
    user_events = {}
    with open(filename, "r") as f:
        for line in f:
            parts = line.split(",")
            user = parts[1].strip()
            event = parts[2].strip()

            if user not in user_events:
                user_events[user] = []

            user_events[user].append(event)
    return user_events


def log_summary(user_events):
    summary = {}
    for user in user_events:
        events = user_events[user]
        summary[user] = {
            "event_count": len(events),
            "has_login": "login" in events,
            "has_logout": "logout" in events
        }
    return summary

# ========================================================================
# CSV FILE PROCESSING (WITHOUT PANDAS)
# ========================================================================

import csv

def read_csv_column(filename, column_name):
    values = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            values.append(float(row[column_name]))
    return values


def csv_column_stats(filename, column_name):
    values = read_csv_column(filename, column_name)
    return {
        "count": len(values),
        "mean": mean_list(values),
        "min": min_list(values),
        "max": max_list(values)
    }

# ========================================================================
# LEDGER / TRANSACTION FILE PROCESSING
# Format: transaction_id, account_id, amount
# ========================================================================

def read_ledger(filename):
    account_data = {}
    with open(filename, "r") as f:
        for line in f:
            parts = line.split(",")
            account = parts[1].strip()
            amount = int(parts[2].strip())

            if account not in account_data:
                account_data[account] = []

            account_data[account].append(amount)
    return account_data


def ledger_summary(account_data):
    summary = {}
    for account in account_data:
        balance = 0
        ever_negative = False

        for amt in account_data[account]:
            balance = balance + amt
            if balance < 0:
                ever_negative = True

        summary[account] = {
            "final_balance": balance,
            "transaction_count": len(account_data[account]),
            "ever_negative": ever_negative
        }
    return summary

# ========================================================================
# JSON EXPORT
# ========================================================================

import json

def write_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

# ========================================================================
# UNIVERSAL EXAM PATTERN (MEMORIZE)
# ========================================================================
# result = {}
# for item in data:
#     if key not in result:
#         result[key] = initial_value
#     result[key] = update
# ========================================================================

# END OF CHEATSHEET
# =========================================================================
