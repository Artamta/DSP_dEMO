import json

# --------------------------------------------------
# FUNCTION 1: Read log file & build user -> events
# --------------------------------------------------
def read_log_file(file_path):
    """
    Reads a log file line by line.
    Returns a dictionary:
    user_id -> list of event types
    """
    user_events = {}

    with open(file_path, "r") as file:
        for line in file:
            # Ignore empty lines
            if not line.strip():
                continue

            # Split by comma
            parts = line.split(",")

            # Extract fields safely
            timestamp = parts[0].strip()
            user_id = parts[1].strip()
            event = parts[2].strip()

            # Initialize list if user seen first time
            if user_id not in user_events:
                user_events[user_id] = []

            # Append event
            user_events[user_id].append(event)

    return user_events


# --------------------------------------------------
# FUNCTION 2: Build summary per user
# --------------------------------------------------
def build_summary(user_events):
    """
    Builds summary dictionary of the form:
    user_id -> {event_count, has_login, has_logout}
    """
    summary = {}

    for user in user_events:
        events = user_events[user]

        event_count = len(events)

        # Flags
        has_login = False
        has_logout = False

        for e in events:
            if e == "login":
                has_login = True
            if e == "logout":
                has_logout = True

        summary[user] = {
            "event_count": event_count,
            "has_login": has_login,
            "has_logout": has_logout
        }

    return summary


# --------------------------------------------------
# FUNCTION 3: Write summary to JSON
# --------------------------------------------------
def write_json(summary, output_file):
    """
    Writes dictionary to a JSON file
    """
    with open(output_file, "w") as f:
        json.dump(summary, f, indent=4)


# --------------------------------------------------
# MAIN PROGRAM (EXAM FRIENDLY)
# --------------------------------------------------
log_file = "events.log"          # change filename if needed
output_file = "summary.json"     # output JSON

user_events = read_log_file(log_file)
summary = build_summary(user_events)
write_json(summary, output_file)

# Print for verification (optional in exam)
for user in summary:
    print(user, "->", summary[user])
