# CRZP-Scraping

CRZP-Scraping is a Python-based web scraping tool designed to extract thesis information from the opac.crzp.sk website. This tool reads a list of thesis URLs in a CSV file, scrapes the relevant thesis metadata from each link, and exports the extracted data into a CSV file.


The scraped information includes the following thesis details:

- **TYPE**: The type of thesis (e.g., Bachelor's, Master's, Doctoral).
- **NAME**: The title of the thesis.
- **AUTHOR**: The name of the thesis author.
- **SUPERVISOR**: The name of the thesis supervisor.
- **CONSULTANT**: The name of the thesis consultant (if available).
- **YEAR**: The year the thesis was published.
- **SCHOOL**: The university or institution where the thesis was submitted.
- **KEYWORDS**: A list of keywords associated with the thesis.
- **ABSTRACT_1**: The abstract of the thesis in the first available language.
- **ABSTRACT_2**: The abstract of the thesis in the second available language (if applicable).


## Dependencies

- **Python 3.x**
- **requests** – For sending HTTP requests to the CRZP website.
- **beautifulsoup4** – For parsing the HTML content.
- **csv** – For working with CSV files.
- **time** – Pause between requests.

## Usage

Prepare the input CSV file:

url_links.csv: The CSV file containing the URLs of the theses.

Run the code

Review the output CSV file for the extracted thesis details.
