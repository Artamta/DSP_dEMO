import json

# Dictionary to map user -> list of events
user_events = {}

# Step 1 & 2: Read file line by line and build user -> events list
with open("sample/events.log", "r") as file:
    for line in file:
        parts = line.split(",")

        timestamp = parts[0].strip()
        user = parts[1].strip()
        event = parts[2].strip()

        # If user not seen before, create empty list
        if user not in user_events:
            user_events[user] = []

        # Add event to user's event list
        user_events[user].append(event)
#for u in user_events:
#    print(u,user_events[u])
# Step 3 & 4: Create summary dictionary
summary = {}

for user in user_events:
    events = user_events[user]

    event_count = len(events)

    # Check if user has logged in at least once
    has_login = False
    for e in events:
        if e == "login":
            has_login = True
            break

    # Store summary for this user
    summary[user] = {
        "event_count": event_count,
        "has_login": has_login
    }

# Step 5: Write summary to JSON file
with open("summary.json", "w") as json_file:
    json.dump(summary, json_file, indent=4)

print("Summary written to summary.json")
