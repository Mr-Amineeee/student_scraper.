

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import URL, TIMEOUT, CSV_FILE
import logging
from selenium.common.exceptions import TimeoutException
from pathlib import Path
from datetime import datetime

from scraper import (
    get_table_headers,
    scrape_current_page,
    get_page_info,
    go_to_next_page
)

from utils import save_to_csv

Path("data").mkdir(exist_ok=True)
Path("logs").mkdir(exist_ok=True)
Path("screenshots").mkdir(exist_ok=True)

logging.basicConfig(
    filename="logs/scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

driver = webdriver.Chrome()




try:
      
    logging.info("Browser started")

    driver.get(URL)

    logging.info("Website opened")

    wait = WebDriverWait(driver, TIMEOUT)

    table = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "table")
        )
    )

    logging.info("Table found")

    table_data = []

    header_names = get_table_headers(driver)

    while True:

        page_data = scrape_current_page(
            driver,
            header_names
        )

        table_data.extend(page_data)

        page_info = get_page_info(
            driver,
            table
        )

        current_page = page_info["page"]
        total_pages = page_info["pages"]

        print(
            f"Scraped page {current_page + 1} "
            f"of {total_pages}"
        )

        logging.info(
            f"Scraped page {current_page + 1} "
            f"of {total_pages}"
        )

        if current_page >= total_pages - 1:
            break

        go_to_next_page(
            driver,
            table,
            current_page,
            wait
        )

    save_to_csv(
        table_data,
        CSV_FILE
    )

    logging.info("CSV file created successfully")
    logging.info(
        f"Total rows scraped: {len(table_data)}"
    )

    print("Total rows:", len(table_data))


except TimeoutException as error:

    logging.error(
        f"Scraper failed: {error}"
    )

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    screenshot_path = (Path("screenshots")/ f"error_{timestamp}.png")

    driver.save_screenshot(screenshot_path)


finally:

    driver.quit()
    logging.info("Browser closed")
