import csv

input_csv = 'jobs.csv'
output_csv = 'jobs_clean.csv'

input_csv_path = f'/home/fabioski01/careers-html-csv/{input_csv}'
output_csv_path = f'/home/fabioski01/careers-html-csv/{output_csv}'
# Read and process the CSV
with open(input_csv_path, 'r', encoding='utf-8') as infile, open(output_csv_path, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()

    for row in reader:
        # Process each field to remove extra quotes
        row['Job Title'] = row['Job Title'].strip('" ')
        row['Vacancy Type'] = row['Vacancy Type'].strip('" ')
        row['Closing Date'] = row['Closing Date'].strip('" ')
        row['Workplace'] = row['Workplace'].strip('" ')
        writer.writerow(row)

print(f"Cleaned CSV saved to {output_csv_path}")