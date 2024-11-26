from bs4 import BeautifulSoup
import csv

# Load the HTML file
html_file_path = '/home/fabioski01/careers-html-csv/ESA_Jobs_clean.html'  # Replace with the path to your HTML file
with open(html_file_path, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Extract job data
jobs = []
seen_jobs = set()  # To avoid duplicates

for tile in soup.find_all('div', class_='tiletitle'):
    # Extract job title and hyperlink
    title_tag = tile.find('a', class_='jobTitle-link')
    job_title = title_tag.get_text(strip=True) if title_tag else 'N/A'
    hyperlink = title_tag['href'] if title_tag else 'N/A'

    # Avoid duplicates using the job title as a unique identifier
    if job_title in seen_jobs:
        continue
    seen_jobs.add(job_title)

    # Find the next 'oneline' div for the details
    details_div = tile.find_next('div', class_='oneline')

    # Extract vacancy type
    vacancy_type = 'N/A'
    if details_div:
        vacancy_div = details_div.find('div', id=lambda x: x and 'desktop-section-shifttype' in x)
        if vacancy_div:
            vacancy_type = vacancy_div.find('div').get_text(strip=True)

    # Extract closing date
    closing_date = 'N/A'
    if details_div:
        closing_div = details_div.find('div', id=lambda x: x and 'desktop-section-department' in x)
        if closing_div:
            closing_date = closing_div.find('div').get_text(strip=True)

    # Extract workplace
    workplace = 'N/A'
    if details_div:
        workplace_div = details_div.find('div', id=lambda x: x and 'desktop-section-multilocation' in x)
        if workplace_div:
            workplace = workplace_div.find('div').get_text(strip=True)

    # Append job details to the list
    jobs.append({
        'Job Title': job_title,
        'Hyperlink': hyperlink,
        'Vacancy Type': vacancy_type,
        'Closing Date': closing_date,
        'Workplace': workplace
    })

# Write to CSV
csv_file_path = 'jobs.csv'  # Replace with your desired file path
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['Job Title', 'Hyperlink', 'Vacancy Type', 'Closing Date', 'Workplace'])
    writer.writeheader()
    writer.writerows(jobs)

print(f"Data successfully saved to {csv_file_path}")