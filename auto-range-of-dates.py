from datetime import datetime, timedelta


# Set the start and end dates
start_date = datetime(2024, 2, 6)  # yyyy, m, d
end_date =   datetime(2024, 2, 8)   # yyyy, m, d

commits=(12,16) #no of commits will be randomly picked in this range



"---------------------====== Driver Code Below ======---------------------"
import subprocess, random
# Specifing the base time for commits (random time)
base_time = timedelta(hours=random.randint(8,12), minutes=random.randint(1,59), seconds=random.randint(1,59))

# Creating a new file for changes
with open("example.txt", "w") as f:
    f.write("Initial content")

# Iterating through the date range
current_date = start_date
while current_date <= end_date:
    num_commits = random.randint(commits[0],commits[1])
    for i in range(num_commits):
        # Calculate the commit date for the current iteration
        commit_date = datetime.combine(current_date, datetime.min.time()) + base_time + timedelta(hours=i)

        # Generating commit message
        commit_message = f'Commit {i + 1} on {commit_date}'

        # Making changes to the file
        with open("example.txt", "a") as f:
            f.write(f"\nChange {i + 1} at {commit_date}")

        # Git commands
        subprocess.run(['git', 'add', 'example.txt'])
        subprocess.run(['git', 'commit', '--date', commit_date.strftime('%Y-%m-%dT%H:%M:%S'), '-m', commit_message])

    # Finally Pushing commits to the remote repository after each day's commits
    subprocess.run(['git', 'push'])
    print("\n\t \t", current_date)

    # Move to the next date
    current_date += timedelta(days=1)
