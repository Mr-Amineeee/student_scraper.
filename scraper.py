from selenium.webdriver.common.by import By


def get_table_headers(driver):

    headers = driver.find_elements(
        By.CSS_SELECTOR,
        "table thead th"
    )

    header_names = [
        header.text.strip()
        for header in headers
    ]

    return header_names


def scrape_current_page(driver, header_names):

    rows = driver.find_elements(
        By.CSS_SELECTOR,
        "table tbody tr"
    )

    page_data = []

    for row in rows:

        cells = row.find_elements(
            By.TAG_NAME,
            "td"
        )

        values = [
            cell.text.strip()
            for cell in cells
        ]

        if values:
            row_dic = dict(
                zip(header_names, values)
            )

            page_data.append(row_dic)

    return page_data


def get_page_info(driver, table):

    page_info = driver.execute_script("""
        return window.jQuery(arguments[0])
            .DataTable()
            .page.info();
    """, table)

    return page_info


def go_to_next_page(driver, table, current_page, wait):

    driver.execute_script("""
        window.jQuery(arguments[0])
            .DataTable()
            .page("next")
            .draw("page");
    """, table)

    wait.until(
        lambda d:
        d.execute_script("""
            return window.jQuery(arguments[0])
                .DataTable()
                .page.info()
                .page;
        """, table) > current_page
    )