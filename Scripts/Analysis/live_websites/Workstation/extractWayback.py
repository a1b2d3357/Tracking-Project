import pandas as pd
import regex as re
import os
from tqdm import tqdm


def process_snapshot(snapshot_path):
    pixel_ids = set()

    with open(snapshot_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Pattern 1: Extract IDs from script src pattern
    script_pattern = r'<script src="https://connect\.facebook\.net/signals/config/(\d+)'
    ids_from_script = re.findall(script_pattern, content)
    pixel_ids.update(ids_from_script)

    # Pattern 2: Extract IDs from fbq("init", ...) pattern
    fbq_pattern = r'fbq\("init","(\d+)"\);'
    ids_from_fbq = re.findall(fbq_pattern, content)
    pixel_ids.update(ids_from_fbq)

    # Return the list of unique IDs
    return list(pixel_ids)


def create_dataframe(base_folder):
    # Generate all months from Sept 2024 to Sept 2019
    months = pd.date_range(start="2019-09-01", end="2024-09-01", freq='MS').strftime("%Y%m").tolist()[::-1]
    data = []
    websites = [website for website in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, website))]
    for website in tqdm(websites, desc="Processing websites", unit="website"):
        website_path = os.path.join(base_folder, website)
        
        # Create a dictionary to store the results for this website
        results = {"website": website}
        
        # Initialize each month with None for this website
        for month in months:
            results[month] = None
        
        for snapshot in os.listdir(website_path):
            snapshot_timestamp = snapshot[:6]  # Extract the year and month from the filename
            snapshot_path = os.path.join(website_path, snapshot)

            # If the snapshot timestamp matches one of the months, process it
            if snapshot_timestamp in results:
                result = process_snapshot(snapshot_path)
                results[snapshot_timestamp] = result if result else []

        data.append(results)

    df = pd.DataFrame(data)
    df.to_csv("pixelHistory.csv") # don't change

    return df

base_folder = "../Parallel-Scripts/Server 1" #configure this to where all downloaded snapshots are
df = create_dataframe(base_folder)