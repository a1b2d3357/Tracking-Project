from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from datetime import datetime, timedelta
import os
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from dateutil.relativedelta import relativedelta
from selenium.common.exceptions import TimeoutException, WebDriverException


def add_month(date_str):
    date_obj = datetime.strptime(date_str, '%Y%m%d')
    new_date_obj = date_obj + relativedelta(months=1)
    new_date_str = new_date_obj.strftime('%Y%m%d')
    return new_date_str

# Function to get snapshots with pagination
def get_all_snapshots(url, start_date, end_date, limit=100000):
    all_snapshots = []
    current_start = start_date
    while current_start <= end_date:
        api_url = f"http://web.archive.org/cdx/search/cdx?url={url}&from={current_start}&to={end_date}&output=json&limit={limit}"
        for i in range(5): #max tries are 5
            try:
                response = requests.get(api_url)
                
                if response.status_code == 200:
                    data = response.json()
                    snapshots = data[1:]  # Excluding the header
                    if not snapshots:
                        print("No snapshots to fetch")
                        current_start = add_month(end_date)
                        break
                    monthly_end = snapshots[-1][1][:8]  # Use the timestamp of the last snapshot to set the new start date
                    if monthly_end !=current_start:
                        current_start = monthly_end

                    all_snapshots.append(filter_snapshots_by_month(snapshots))
                    break
            
                else:
                    print("Failed to fetch data")
                    continue
            except:
                continue
        current_start = add_month(current_start)

        


    return all_snapshots

# Function to filter snapshots to one per month
def filter_snapshots_by_month(snapshots):
    snapshots_by_month = {}
    
    for snapshot in snapshots:
        timestamp = snapshot[1]
        date_str = timestamp[:6]  # Extract YYYYMM
        if date_str not in snapshots_by_month:
            snapshots_by_month[date_str] = snapshot
    
    return snapshots_by_month


# Function to generate a date range
def generate_date_range(years=5):
    current_date = datetime.now()
    start_date = (current_date - timedelta(days=years*365)).strftime('%Y%m%d')
    end_date = current_date.strftime('%Y%m%d')
    return start_date, end_date

def generateAllSnapshots(url):
    start_date, end_date = generate_date_range()
    snapshots = get_all_snapshots(url, start_date, end_date, limit=100000)
    all_snapshots = []
    for snap in snapshots:
        for month, snapshot in snap.items():
            all_snapshots.append(snapshot)
    return all_snapshots


def download_past_versions(website,driver ,max_retries = 5):
    # print(f"Processing {website}")
    wayback_base_url = "https://web.archive.org/web/"

    snapshots = generateAllSnapshots(website)
    print("Generated all snapshots")
    if snapshots:
        for snapshot in snapshots:

            timestamp = snapshot[1]
            original_url = snapshot[2]
            wayback_url = f"{wayback_base_url}{timestamp}/{original_url}" #A resource at the wayback has a url of this format
            wayback_timestamp = snapshot[1]
            # print(f"Downloading snapshot: {wayback_url}")

            mount_path = f"/mnt/data0/yvekaria/PixelWorld/PixelWayback/top10k_snapshots/{website}"
            if (not os.path.exists(mount_path)):
                os.makedirs(mount_path, exist_ok=True)

            filename = f"{wayback_timestamp}.html"
            filepath = os.path.join(mount_path,filename)
        
            for attempt in range(max_retries):
                # print(f"Attempt {attempt + 1}: Getting snapshot for {wayback_timestamp}")
            
                try:
                    driver.get(wayback_url)
                    page_source = driver.page_source

                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(page_source)
                    print(f"Downloaded and saved: {filepath}")
                    break
                except requests.exceptions.RequestException as e:
                    print(f"Error downloading {wayback_url}: {e}")
                    time.sleep(5)
                except TimeoutException as e:
                    print(f"TimeoutException on attempt {attempt + 1} for {wayback_url}: {e}")
                    time.sleep(5)  # Retry after a delay
                    break
                except WebDriverException as e:
                    print(f"WebDriverException on attempt {attempt + 1} for {wayback_url}: {e}")
                    time.sleep(5)
                except Exception as e:
                    print(f"General error on attempt {attempt + 1} for {wayback_url}: {e}")
                    time.sleep(5)
    

    else:
        print(f"No snapshots available for {website}")

    return None, None

def load_progress(filename):
    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        return pd.DataFrame(columns=["Website Name", "Completed"])

def save_progress(df, filename):
    df.to_csv(filename, index=False)


def crawlWayback(urls, progress_file):
    # Load previous progress if any
    progress_df = load_progress(progress_file)
    completed_urls = progress_df['Website Name'].tolist()

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


    total_urls = len(urls)
    
    for idx, website in enumerate(urls):
        if website in completed_urls:
            print(f"Skipping {website}, already processed.")
            continue
        print("Processing ",website)
        
        download_past_versions(website,driver)    
        # Save progress after each URL is processed
        record = [website,"completed"]
        progress_df.loc[len(progress_df)] = record

        save_progress(progress_df, progress_file)
        # Print progress
        print(f"Processed {idx + 1}/{total_urls}: {website}")

    driver.quit()
    return progress_df

urls = pd.read_csv('tranco_10k_1.csv')['website'].to_list()
progress_file = "progress.csv"
crawlWayback(urls,progress_file)