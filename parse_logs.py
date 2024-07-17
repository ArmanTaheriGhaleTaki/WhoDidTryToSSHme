import re
import pandas as pd
import psycopg2
# Define regex pattern for parsing
log_pattern = re.compile(
    r'^(?P<month>\w+)\s+(?P<day>\d+)\s+(?P<time>\d+:\d+:\d+)\s+\S+\s+\S+\[\d+\]:\s+.+user\s(?P<username>\w+)\s(?P<ip_address>\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})\sport\s\d+\s\[preauth\]$'
    # r'^(?P<month>\w+)\s+(?P<day>\d+)\s+(?P<time>\d+:\d+:\d+)\s+\S+\s+\S+\[\d+\]:\s+(?P<message>.*)$'
    # r'^(?P<month>\w+)\s+(?P<day>\d+)\s+(?P<time>\d+:\d+:\d+)\s+(?P<hostname>\S+)\s+(?P<process>\S+)\[(?P<pid>\d+)\]:\s+(?P<message>.*)$'
)

# Read the log file
log_file_path = 'auth.log'
with open(log_file_path, 'r') as file:
    log_lines = file.readlines()

# Parse the log lines
parsed_logs = []
for line in log_lines:
    match = log_pattern.match(line)
    if match:
        parsed_logs.append(match.groupdict())

# Convert to DataFrame
df = pd.DataFrame(parsed_logs)
# print(df.head())
print(df)
db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost'
}
conn = psycopg2.connect(**db_params)
cur = conn.cursor()
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO parsed_data (month, day, time, username, ip_address)
        VALUES (%s, %s, %s, %s, %s);
    """, (row['month'], int(row['day']), row['time'], row['username'], row['ip_address']))
    conn.commit()
