import subprocess
from datetime import datetime, timedelta

# Specify the number of commits and the base date
num_commits = 11
base_date = datetime(2023, 9, 24, 4, 0, 0) #yyyy m d h m s , 6 aug

# Create a new file for changes
with open("example.txt", "w") as f:
    f.write("Initial content")

for i in range(num_commits):
    # Calculate the date for the current commit
    commit_date = base_date + timedelta(hours=i)

    # Generate commit message
    commit_message = f'Commit {i + 1} on {commit_date}'

    # Make changes to the file
    with open("example.txt", "a") as f:
        f.write(f"\nChange {i + 1} at {commit_date}")

    # Git commands
    subprocess.run(['git', 'add', 'example.txt'])
    subprocess.run(['git', 'commit', '--date', commit_date.strftime('%Y-%m-%dT%H:%M:%S'), '-m', commit_message])
    subprocess.run(['git', 'push'])
    print("\t \t",num_commits-i)
# Push all commits to the remote repository

