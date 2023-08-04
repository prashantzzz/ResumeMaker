import subprocess
from datetime import datetime, timedelta

# Specify the number of commits and the base date
num_commits = 20
base_date = datetime(2023, 8, 4, 12, 0, 0)

for i in range(num_commits):
    # Calculate the date for the current commit
    commit_date = base_date + timedelta(hours=i)

    # Generate commit message
    commit_message = f'Commit {i + 1} on {commit_date}'

    # Git commands
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '--date', commit_date.strftime('%Y-%m-%dT%H:%M:%S'), '-m', commit_message])

# Push all commits to the remote repository
subprocess.run(['git', 'push'])
