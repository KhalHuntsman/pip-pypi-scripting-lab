from datetime import datetime
import os

def generate_log(data):
    # Validate that the input is a list; tests expect a ValueError otherwise.
    if not isinstance(data, list):
        raise ValueError("Input must be a list.")

    # Build a filename using today's date in YYYYMMDD format.
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"

    # Write each log entry to the file, one per line.
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # Return the filename so tests can verify and clean it up.
    return filename
