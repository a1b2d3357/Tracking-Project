import pandas as pd
import regex as re
import os
from tqdm import tqdm

def process_snapshot(snapshot_path):
    pixel_ids = set()

    # Read the HTML content from the file
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

# Function to process all HTML files in a folder and generate the CSV
def generate_pixel_ids_csv(folder_path, output_csv):
    # List to store the data
    data = []

    # Get all HTML files from the folder
    html_files = [file_name for file_name in os.listdir(folder_path) if file_name.endswith('.html')]

    for file_name in tqdm(html_files, desc="Processing HTML files"):
        file_path = os.path.join(folder_path, file_name)
        
        # Get the website name from the HTML file name (without the '.html' extension)
        website_name = os.path.splitext(file_name)[0]
        
        # Process the HTML file to extract pixel IDs
        pixel_ids = process_snapshot(file_path)
        
        # Add the website name and the pixel IDs to the data list
        data.append([website_name, pixel_ids])

    df = pd.DataFrame(data, columns=['Website', 'Pixel IDs'])
    df.to_csv(output_csv, index=False)

folder_path = 'live_websites' #change as per your reqs
output_csv = 'pixelHistoryLive.csv' #don't change

# Run the function to generate the CSV
generate_pixel_ids_csv(folder_path, output_csv)

