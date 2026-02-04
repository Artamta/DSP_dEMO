# =============================================================================
# PYTHON DATA HANDLING MASTER CHEATSHEET (EXAM SAFE)
# =============================================================================
# Covers:
# - Text files, CSV files, log files
# - String parsing (split / strip / csv / regex)
# - Dictionaries vs lists (WHEN and WHY)
# - Grouping, counting, statistics
# - Single-pass (memory safe) & multi-pass methods
# - JSON output
#
# Copy this file in exam and MODIFY SMALL PARTS ONLY.
# =============================================================================

# =============================================================================
# 0. IMPORTS (SAFE STANDARD LIBRARY ONLY)
# =============================================================================

import csv
import json
import re
from collections import defaultdict, Counter, deque
from pathlib import Path

# =============================================================================
# 1. FILE BASICS (READ / WRITE)
# =============================================================================

def read_file_line_by_line(filename):
    """
    Safest way to read a file.
    Use for large files.
    """
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            yield line.rstrip("\n")   # remove newline only


def read_entire_file(filename):
    """
    Use ONLY for small files.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def write_text(filename, text):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)


def append_text(filename, text):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)


# =============================================================================
# 2. STRING PARSING — WHEN TO SPLIT, WHEN NOT TO
# =============================================================================

def parse_simple_csv_line(line):
    """
    Use ONLY when input is guaranteed simple.
    Example: timestamp, user, event
    """
    parts = line.split(",")
    if len(parts) < 3:
        return None
    return parts[0].strip(), parts[1].strip(), parts[2].strip()


def parse_csv_with_module(filename):
    """
    Use when commas, quotes, or real CSV is involved.
    """
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            yield row


def parse_csv_dict(filename):
    """
    Best for column-based CSV questions.
    """
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row


def parse_with_regex(line):
    """
    Use when format is irregular (logs).
    """
    pattern = r"(\S+),\s*(\S+),\s*(\S+)"
    match = re.match(pattern, line)
    if match:
        return match.groups()
    return None


# =============================================================================
# 3. LIST UTILITIES (BASIC STATS)
# =============================================================================

def list_sum(lst):
    total = 0
    for x in lst:
        total += x
    return total


def list_mean(lst):
    return list_sum(lst) / len(lst) if lst else None


def list_min(lst):
    m = lst[0]
    for x in lst:
        if x < m:
            m = x
    return m


def list_max(lst):
    m = lst[0]
    for x in lst:
        if x > m:
            m = x
    return m


def list_variance(lst):
    mean = list_mean(lst)
    total = 0
    for x in lst:
        total += (x - mean) ** 2
    return total / len(lst)


# =============================================================================
# 4. DICTIONARIES — WHEN TO USE WHAT
# =============================================================================
# dict          → simple mapping
# defaultdict   → grouping
# Counter       → frequency counting

def frequency_list(lst):
    freq = {}
    for x in lst:
        if x not in freq:
            freq[x] = 0
        freq[x] += 1
    return freq


def frequency_list_counter(lst):
    return Counter(lst)


# =============================================================================
# 5. LOG FILE TEMPLATE (Exercise 5 TYPE)
# =============================================================================
# Format: timestamp, user_id, event

def log_user_events(filename):
    """
    user_id -> list of events
    """
    user_events = defaultdict(list)

    for line in read_file_line_by_line(filename):
        parsed = parse_simple_csv_line(line)
        if not parsed:
            continue
        _, user, event = parsed
        user_events[user].append(event)

    return user_events


def log_summary(user_events):
    """
    user -> {event_count, has_login, has_logout}
    """
    summary = {}

    for user, events in user_events.items():
        summary[user] = {
            "event_count": len(events),
            "has_login": "login" in events,
            "has_logout": "logout" in events
        }

    return summary


# SINGLE-PASS VERSION (BETTER IN EXAMS)
def log_summary_single_pass(filename):
    count = defaultdict(int)
    has_login = defaultdict(bool)
    has_logout = defaultdict(bool)

    for line in read_file_line_by_line(filename):
        parsed = parse_simple_csv_line(line)
        if not parsed:
            continue
        _, user, event = parsed
        count[user] += 1
        if event == "login":
            has_login[user] = True
        if event == "logout":
            has_logout[user] = True

    return {
        user: {
            "event_count": count[user],
            "has_login": has_login[user],
            "has_logout": has_logout[user]
        }
        for user in count
    }


# =============================================================================
# 6. CSV COLUMN-WISE STATISTICS (Exercise 6 TYPE)
# =============================================================================

def csv_column_stats(filename):
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        columns = reader.fieldnames

        values = {col: [] for col in columns}

        for row in reader:
            for col in columns:
                if row[col].strip() != "":
                    values[col].append(float(row[col]))

    stats = {}
    for col, vals in values.items():
        stats[col] = {
            "count": len(vals),
            "mean": list_mean(vals),
            "min": list_min(vals) if vals else None,
            "max": list_max(vals) if vals else None
        }

    return stats


# MEMORY-SAFE SINGLE PASS VERSION
def csv_column_stats_stream(filename):
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        cols = reader.fieldnames

        count = {c: 0 for c in cols}
        total = {c: 0.0 for c in cols}
        minv = {c: None for c in cols}
        maxv = {c: None for c in cols}

        for row in reader:
            for c in cols:
                if row[c].strip() == "":
                    continue
                x = float(row[c])
                count[c] += 1
                total[c] += x
                minv[c] = x if minv[c] is None else min(minv[c], x)
                maxv[c] = x if maxv[c] is None else max(maxv[c], x)

    return {
        c: {
            "count": count[c],
            "mean": total[c] / count[c] if count[c] else None,
            "min": minv[c],
            "max": maxv[c]
        }
        for c in cols
    }


# =============================================================================
# 7. TRANSACTION LEDGER (Exercise 7 TYPE)
# =============================================================================
# Format: transaction_id, account_id, amount

def ledger_summary(filename):
    accounts = defaultdict(list)

    for line in read_file_line_by_line(filename):
        parts = line.split(",")
        if len(parts) < 3:
            continue
        account = parts[1].strip()
        amount = int(parts[2].strip())
        accounts[account].append(amount)

    summary = {}
    for acc, amounts in accounts.items():
        balance = 0
        ever_negative = False
        for a in amounts:
            balance += a
            if balance < 0:
                ever_negative = True

        summary[acc] = {
            "final_balance": balance,
            "ever_negative": ever_negative,
            "transaction_count": len(amounts)
        }

    return summary


# =============================================================================
# 8. JSON OUTPUT (FINAL STEP IN MOST QUESTIONS)
# =============================================================================

def write_json(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True)


# =============================================================================
# 9. COMMON EXAM PATTERNS (MENTAL TEMPLATES)
# =============================================================================

"""
PATTERN A: GROUPING
-------------------
result = defaultdict(list)
for item in data:
    result[key].append(value)

PATTERN B: COUNTING
-------------------
count = defaultdict(int)
for item in data:
    count[key] += 1

PATTERN C: STREAMING STATS
-------------------------
count, sum, min, max updated per row

PATTERN D: FINAL JSON
---------------------
json.dump(summary, file, indent=2)
"""

# =============================================================================
# END OF CHEATSHEET
# =============================================================================
