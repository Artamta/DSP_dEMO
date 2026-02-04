import csv
import json

# --------------------------------------------------
# FUNCTION 1: Read CSV and collect values column-wise
# --------------------------------------------------
def read_csv_columns(file_path):
    """
    Reads CSV using DictReader.
    Returns a dictionary:
    column_name -> list of numeric values
    """
    column_data = {}

    with open(file_path, "r") as file:
        reader = csv.DictReader(file)

        # Dynamically get column names
        columns = reader.fieldnames

        # Initialize empty list for each column
        for col in columns:
            column_data[col] = []

        # Read rows
        for row in reader:
            for col in columns:
                value = float(row[col])
                column_data[col].append(value)

    return column_data


# --------------------------------------------------
# FUNCTION 2: Compute statistics for each column
# --------------------------------------------------
def compute_statistics(column_data):
    """
    Computes count, mean, min, max for each column.
    Returns:
    column -> {count, mean, min, max}
    """
    stats = {}

    for col in column_data:
        values = column_data[col]

        count = len(values)
        total = sum(values)
        mean = total / count
        minimum = min(values)
        maximum = max(values)

        stats[col] = {
            "count": count,
            "mean": mean,
            "min": minimum,
            "max": maximum
        }

    return stats


# --------------------------------------------------
# FUNCTION 3: Write statistics to JSON
# --------------------------------------------------
def write_json(data, output_file):
    """
    Writes dictionary to JSON file
    """
    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)


# --------------------------------------------------
# MAIN PROGRAM (EXAM FRIENDLY)
# --------------------------------------------------
csv_file = "data.csv"               # input CSV file
output_file = "column_stats.json"   # output JSON file

column_data = read_csv_columns(csv_file)
stats = compute_statistics(column_data)
write_json(stats, output_file)

# Print for verification
for col in stats:
    print(col, "->", stats[col])
