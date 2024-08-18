import requests
import os
import time

#Returns a list of all cdx records of a website (also saves them in a text file)
def getCdxRecords(url):
    base_url = "https://web.archive.org/cdx/search/cdx" # Base URL of the CDX Server API
    params = {
        'url': url,  # URL to fetch
        'output': 'json',      # Output format
        'matchType': 'prefix'  # Match URLs that start with this prefix
        #no limit variable to fetch as many versions available
    }

    # GET request to the API
    response = requests.get(base_url, params=params) # each esponse contains the following information: ["urlkey","timestamp","original","mimetype","statuscode","digest","length"]

    allCdxRecords = []
    # Checks whether the requeust was successful
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        with open('pixelRecords.txt','w') as f:
            for record in data:
                f.write(f"{record}\n")
                allCdxRecords.append(record)
                # Each record represents an archived version
    else:
        print(f"Failed to retrieve data: {response.status_code}")
    return allCdxRecords

# #downloads all webpages inside the all_archives_versions folder 
def downloadArchivedVersions():
    wayback_base_url = "https://web.archive.org/web/"
    save_dir = "archived_versions"
    os.makedirs(save_dir, exist_ok=True)

    with open('pixelRecords.txt', 'r') as f:
        records = f.readlines()

    for record in records:
        record = eval(record.strip())  # Convert the string back to a list
        timestamp = record[1]
        original_url = record[2]

        wayback_url = f"{wayback_base_url}{timestamp}/{original_url}" #A resource at the wayback has a url of this format
        filename = f"{timestamp}.html"
        filepath = os.path.join(save_dir, filename)

        # Check if file already exists
        if os.path.exists(filepath):
            print(f"File already exists: {filepath}") #to continue from saved progress
            continue

        while True:
            try:
                response = requests.get(wayback_url)
                if response.status_code == 200:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(response.text)
                    print(f"Downloaded and saved: {filepath}")
                    break
                elif response.status_code == 404:
                    print(f"File not found (404): {wayback_url}. Skipping...")
                    break  # Stop retrying on 404 errors since it just doesn't exist
                else:
                    print(f"Failed to download {wayback_url}: {response.status_code}")
                    time.sleep(5) #wait before retrying
            except requests.exceptions.RequestException as e:
                print(f"Error downloading {wayback_url}: {e}")
                time.sleep(5)


# Example usage
url = "https://connect.facebook.net/signals/config/1264059003707256" #the url of the meta pixel
getCdxRecords(url)
downloadArchivedVersions()

