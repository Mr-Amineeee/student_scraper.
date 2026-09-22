# Student Scraper

A Python web scraping automation project built with **Selenium** to collect student data from a dynamic paginated table and export the results to CSV.

The project demonstrates practical Selenium automation techniques including explicit waits, dynamic pagination handling, structured data extraction, logging, error handling, and automated screenshots.

## Features

* 🔎 Scrapes student data from a dynamic HTML table
* 📄 Automatically handles multiple pagination pages
* ⏳ Uses `WebDriverWait` for reliable synchronization
* 📊 Converts scraped table data into structured Python dictionaries
* 📁 Exports collected data to CSV
* 📝 Maintains application logs
* 🛡️ Handles Selenium timeout errors
* 📸 Automatically captures screenshots when an error occurs
* ⚙️ Uses a modular project structure
* 🧩 Separates configuration, scraping logic, and utility functions
* 🔧 Uses `pathlib` for cross-platform file path management

## Technologies Used

* Python 3
* Selenium
* CSV
* pathlib
* Logging
* WebDriverWait
* Git
* GitHub

## Project Structure

```text
student_scraper/
├── main.py
├── scraper.py
├── utils.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
├── logs/
└── screenshots/
```

### File Responsibilities

| File / Folder      | Description                                     |
| ------------------ | ----------------------------------------------- |
| `main.py`          | Main entry point of the scraper                 |
| `scraper.py`       | Contains table scraping and pagination logic    |
| `utils.py`         | Contains utility functions such as CSV export   |
| `config.py`        | Stores project configuration                    |
| `requirements.txt` | Lists Python dependencies                       |
| `data/`            | Stores scraped CSV files                        |
| `logs/`            | Stores application logs                         |
| `screenshots/`     | Stores screenshots captured during errors       |
| `.gitignore`       | Prevents unnecessary files from being committed |
| `README.md`        | Project documentation                           |

## How It Works

The scraper follows this workflow:

```text
Open Website
     ↓
Locate Student Table
     ↓
Extract Table Headers
     ↓
Scrape Current Page
     ↓
Check Pagination
     ↓
Move to Next Page
     ↓
Repeat Until Last Page
     ↓
Save Data to CSV
     ↓
Write Logs
```

## Installation

Clone the repository and enter the project directory:

```bash
git clone https://github.com/Mr-Amineeee/student_scraper..git
cd student_scraper
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the scraper with:

```bash
python main.py
```

The scraper will:

1. Open the target website.
2. Locate the student table.
3. Extract the table headers.
4. Scrape the student data.
5. Navigate through all available pages.
6. Collect the results into Python data structures.
7. Export the data to CSV.
8. Write execution information to the log file.
9. Capture a screenshot automatically if a timeout error occurs.
10. Close the browser safely.

## Output

Scraped data is saved to:

```text
data/students.csv
```

Application logs are saved to:

```text
logs/scraper.log
```

Error screenshots are saved to:

```text
screenshots/
```

## Error Handling

The scraper includes error handling designed to make the automation more reliable and easier to debug.

When a timeout occurs:

* The error is recorded in the log file.
* A timestamped screenshot is created.
* The browser is closed safely using `finally`.
* The program exits cleanly.

Example:

```python
except TimeoutException as error:
    logging.error(f"Scraper failed: {error}")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    screenshot_path = (
        Path("screenshots")
        / f"error_{timestamp}.png"
    )

    driver.save_screenshot(screenshot_path)
```

## Key Selenium Concepts Demonstrated

This project demonstrates several important Selenium concepts:

* `webdriver.Chrome()`
* `find_element()`
* `find_elements()`
* CSS selectors
* `WebDriverWait`
* Explicit expected conditions
* JavaScript execution
* DataTables pagination
* Dynamic page synchronization
* Table row extraction
* Browser lifecycle management
* Exception handling
* Screenshots

## Data Processing

Table rows are converted into dictionaries using the extracted headers.

For example:

```python
row_data = dict(
    zip(header_names, values)
)
```

This produces structured data similar to:

```python
{
    "Student Name": "John Doe",
    "Gender": "Male",
    "Class Level": "Senior",
    "Home State": "California"
}
```

The collected rows are then written to CSV using Python's `csv.DictWriter`.

## Reliability

Instead of relying on fixed delays such as:

```python
time.sleep(3)
```

the project uses explicit waits and state-based synchronization.

This makes the automation more reliable when page loading times vary.

## Future Improvements

Possible future improvements include:

* [ ] Add command-line arguments
* [ ] Add configurable browser options
* [ ] Add retry mechanisms
* [ ] Add automated tests
* [ ] Add duplicate-data detection
* [ ] Add Excel export
* [ ] Add database storage
* [ ] Add API integration
* [ ] Add CI/CD automation
* [ ] Add AI-powered data processing

## Learning Goals

This project was built as part of a practical learning path focused on:

**Python → Web Automation → Data Extraction → APIs → AI Automation**

The goal is to progressively transform small automation scripts into maintainable, production-style automation projects.

## Author

**Mohamed Amine**

Python Automation & AI learner focused on building practical automation projects with Python.

## License

This project is intended for educational and portfolio purposes.

