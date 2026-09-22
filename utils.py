import csv


def save_to_csv(table_data, filename):

    if not table_data:
        print("No data to save.")
        return

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=table_data[0].keys()
        )

        writer.writeheader()
        writer.writerows(table_data)

    print("CSV created successfully!")