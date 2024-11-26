from bs4 import BeautifulSoup
import csv

# Load the HTML file
html_file_path = '/home/fabioski01/careers-html-csv/ESA_Jobs_clean.html'  # Replace with the path to your HTML file
with open(html_file_path, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Extract job data
jobs = []

for tile in soup.find_all('div', class_='tiletitle'):
    # Extract job title and hyperlink
    title_tag = tile.find('a', class_='jobTitle-link')
    job_title = title_tag.get_text(strip=True) if title_tag else 'N/A'
    hyperlink = title_tag['href'] if title_tag else 'N/A'

    # Find the parent div to extract additional fields
    parent_div = tile.find_next('div', class_='oneline')

    # Extract vacancy type
    vacancy_div = parent_div.find('div', class_='section-field shifttype') if parent_div else None
    vacancy_type = vacancy_div.find_next('div').get_text(strip=True) if vacancy_div else 'N/A'

    # Extract closing date
    closing_div = parent_div.find('div', class_='section-field department') if parent_div else None
    closing_date = closing_div.find_next('div').get_text(strip=True) if closing_div else 'N/A'

    # Extract workplace
    workplace_div = parent_div.find('div', class_='section-field multilocation') if parent_div else None
    workplace = workplace_div.find_next('div').get_text(strip=True) if workplace_div else 'N/A'

    # Append to jobs list
    jobs.append({
        'Job Title': job_title,
        'Hyperlink': hyperlink,
        'Vacancy Type': vacancy_type,
        'Closing Date': closing_date,
        'Workplace': workplace
    })

# Write to CSV
csv_file_path = 'jobs.csv'  # Replace with the desired output path
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['Job Title', 'Hyperlink', 'Vacancy Type', 'Closing Date', 'Workplace'])
    writer.writeheader()
    writer.writerows(jobs)

print(f"Data successfully saved to {csv_file_path}")