import json

# --------------------------------------------------
# Function 1: Read log file and build user → events list
# --------------------------------------------------
def read_log_file(file_path):
    """
    Reads the log file line by line and returns a dictionary:
    user_id -> list of event types
    """
    user_events = {}

    with open(file_path, "r") as file:
        for line in file:
            # Split line by comma
            parts = line.split(",")

            # Extract fields
            timestamp = parts[0].strip()
            user = parts[1].strip()
            event = parts[2].strip()

            # Initialize list if user not seen before
            if user not in user_events:
                user_events[user] = []

            # Add event to user's list
            user_events[user].append(event)

    return user_events


# --------------------------------------------------
# Function 2: Build summary dictionary
# --------------------------------------------------
def build_summary(user_events):
    """
    Builds summary dictionary:
    user_id -> {event_count, has_login}
    """
    summary = {}

    for user in user_events:
        events = user_events[user]

        event_count = len(events)

        # Check if login occurred
        has_login = False
        for e in events:
            if e == "login":
                has_login = True
                break

        summary[user] = {
            "event_count": event_count,
            "has_login": has_login
        }

    return summary


# --------------------------------------------------
# Function 3: Write summary to JSON file
# --------------------------------------------------
def write_summary_to_json(summary, output_file):
    """
    Writes summary dictionary to a JSON file
    """
    with open(output_file, "w") as json_file:
        json.dump(summary, json_file, indent=4)


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------
log_file = "sample/events.log"
output_file = "summary.json"

# Step 1: Read log file
user_events = read_log_file(log_file)

# Step 2: Build summary
summary = build_summary(user_events)

# Step 3: Write summary to JSON
write_summary_to_json(summary, output_file)

# Step 4: Print summary (for verification)
print("Summary:")
for user in summary:
    print(user, ":", summary[user])

