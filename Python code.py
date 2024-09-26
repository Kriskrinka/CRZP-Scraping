import csv
import requests
from bs4 import BeautifulSoup
import time

with open('zavp2.csv') as file:
    reader = csv.reader(file)
    urls = [row[0] for row in reader if len(row) > 0]

with open('Dataset1', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    for url in urls:
        response = requests.get(url)
        time.sleep(3)  # Pause for 1 second between requests
        soup = BeautifulSoup(response.content, 'html.parser')

        parent_div = soup.find('div', class_='form-horizontal description-padding')

        type_element = soup.select_one("strong.label.label-success")
        type = type_element.text.strip() if type_element else "None"

        title_element = soup.find('h4', {'class': 'inline bold'})
        title = title_element.text.strip() if title_element else "None"

        author_element = soup.find('dt', string='Autor')
        author = author_element.find_next_sibling('dd').text.strip() if author_element else "None"

        supervisor_element = soup.find('dt', string='Školiteľ')
        supervisor = supervisor_element.find_next_sibling('dd').text.strip() if supervisor_element else "None"

        opponent_element = soup.find('dt', string='Oponent')
        opponent = opponent_element.find_next_sibling('dd').text.strip() if opponent_element else "None"

        school_element = soup.find('dt', string='Škola')
        school = school_element.find_next_sibling('dd').text.strip() if school_element else "None"

        year_element = soup.find('dt', string='Rok odovzdania')
        year = year_element.find_next_sibling('dd').text.strip() if year_element else "None"

        div = soup.find('div', {'class': 'panel-body group line-margin'})
        keywords = [a.text.strip() for a in div.find_all('a', class_='btn')] if div else "None"

        abstracts = []
        for child_div in parent_div.find_all('div', class_='panel panel-default panel-margin'):
            text_element = child_div.find('div', class_='well well-sm')
            text = text_element.text.strip() if text_element else "None"
            abstracts.append(text)

        if len(abstracts) >= 1:
            row = [type, title, author, supervisor, opponent, year, school, keywords] + abstracts
            if len(abstracts) == 1:
                row.append("None")
            writer.writerow(row)
            print('Row written to CSV:', row)
        else:
            print('Error: Could not find both abstracts on', url)