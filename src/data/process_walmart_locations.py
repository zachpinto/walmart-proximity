import csv
import re

# Clean up the data and write to a new CSV file
def process_walmart_data(input_file, output_file):
    with open(input_file, 'r') as file, open(output_file, 'w', newline='') as output:
        writer = csv.writer(output)
        writer.writerow(['State', 'City', 'Address', 'Designation', 'Store #', 'Open Date'])

        current_state = None
        for line in file:
            line = line.strip()
            if line:
                # Check if the line is a state name
                if '-' not in line and '–' not in line:
                    current_state = line
                else:
                    # Normalize different hyphens/dashes for splitting
                    normalized_line = line.replace('–', '-')

                    # Handle special cases explicitly
                    if 'store #' not in normalized_line:
                        normalized_line = re.sub(r'\((store #\d+),', r'- Walmart - \1 -', normalized_line)

                    # Extract store details
                    parts = normalized_line.split(' - ')
                    if len(parts) < 3:
                        print(f"Skipping line due to unexpected format: {line}")
                        continue

                    city = parts[0].strip()
                    address = parts[1].strip()
                    details = ' - '.join(parts[2:]).strip()

                    # Regex to handle variations and extract full date
                    match = re.search(
                        r'(Walmart Supercenter|Walmart|Neighborhood Market|Clinic Pharmacy|Supercenter)? '
                        r'?\(?(store # ?(\d+)), opened (.*? \d{4})',
                        details, re.IGNORECASE)
                    if match:
                        designation = match.group(1) if match.group(1) else 'Walmart'
                        store_num = match.group(3)
                        open_date = match.group(4)  # Capture the date including the year
                        writer.writerow([current_state, city, address, designation, store_num, open_date])
                    else:
                        print(f"Details not matched for line: {line}")

# Usage
process_walmart_data('//data/raw/walmart_locations_raw.txt',
                     '//data/processed/walmart.csv')
