#!/usr/bin/python3
import sys
import re
import signal

# Initialize variables to hold metrics
total_file_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Define a function to handle keyboard interruption
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Define a function to print statistics
def print_stats():
    print("File size: {}".format(total_file_size))
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print("{}: {}".format(status_code, status_counts[status_code]))

# Define the regular expression pattern to match the input format
pattern = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[.+\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$')

# Read from stdin line by line and process the input
for line in sys.stdin:
    match = pattern.match(line.strip())
    if match:
        # Extract relevant data from the line
        file_size = int(match.group(3))
        status_code = int(match.group(2))

        # Update metrics
        total_file_size += file_size
        status_counts[status_code] += 1
        line_count += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_stats()

# Print final statistics
print_stats()

