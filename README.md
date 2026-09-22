# Student Scraper

A Selenium-based web scraper that extracts student data from a paginated table and saves the results to a CSV file.

## Features

- Web scraping with Selenium
- Explicit waits with WebDriverWait
- Table data extraction
- Automatic pagination handling
- CSV export
- Logging
- Error handling
- Automatic error screenshots
- Path management with pathlib

## Installation

### 1. Clone the project

```bash
git clone <repository-url>
cd student_scraper
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows:

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

## Usage

Run the scraper with:

```bash
python main.py
```

The scraper will:

1. Open the target website.
2. Find the student table.
3. Scrape the data from each page.
4. Navigate through all pages automatically.
5. Save the scraped data to a CSV file.
6. Create logs in the `logs/` folder.
7. Take a screenshot automatically if an error occurs.

### Output

The scraped data is saved to:

```text
data/students.csv
```

Logs are saved to:

```text
logs/scraper.log
```

Error screenshots are saved to:

```text
screenshots/
```
## Project Structure

```text
student_scraper/
├── main.py
├── scraper.py
├── utils.py
├── config.py
├── requirements.txt
├── README.md
├── data/
├── logs/
└── screenshots/
```

### Files and folders

* `main.py` — Main entry point of the scraper.
* `scraper.py` — Contains the scraping and pagination functions.
* `utils.py` — Contains utility functions such as CSV export.
* `config.py` — Stores project configuration such as URL, timeout, and file paths.
* `requirements.txt` — Lists the Python dependencies required by the project.
* `README.md` — Project documentation.
* `data/` — Stores the scraped CSV data.
* `logs/` — Stores application logs.
* `screenshots/` — Stores screenshots captured when an error occurs.

## Technologies Used

* Python
* Selenium
* pathlib
* CSV
* Logging
* WebDriverWait
* Git / GitHub

## Error Handling

The scraper includes error handling to make the automation more reliable.

If a timeout or scraping error occurs:

1. The error is recorded in the log file.
2. A screenshot is automatically created.
3. The browser is closed safely.
4. The program exits without leaving the browser running.

This helps make the scraper easier to debug and maintain.
