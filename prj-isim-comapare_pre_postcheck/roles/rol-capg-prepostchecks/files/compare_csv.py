#!/usr/bin/env python3
import csv
import sys

def compare_csv(pre_checks_file, post_checks_file, output_file):
    # Read CSV files
    with open(pre_checks_file, mode='r') as pre_file:
        pre_reader = csv.DictReader(pre_file)
        pre_data = {row['Vserver Name']: row['Vserver State'] for row in pre_reader}

    with open(post_checks_file, mode='r') as post_file:
        post_reader = csv.DictReader(post_file)
        post_data = [row for row in post_reader if pre_data.get(row['Vserver Name']) != row['Vserver State']]

    # Write to output file
    with open(output_file, mode='w', newline='') as output_csv:
        fieldnames = ['Vserver State', 'Vserver State Timestamp', 'Vserver Name']
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)

        writer.writeheader()
        for row in post_data:
            writer.writerow({field: row[field] for field in fieldnames})

if __name__ == "__main__":
    # Command-line arguments
    pre_checks_path = sys.argv[1]
    post_checks_path = sys.argv[2]
    output_path = sys.argv[3]

    # Run the comparison
    compare_csv(pre_checks_path, post_checks_path, output_path)
