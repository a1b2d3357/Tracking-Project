import requests
import os
import time

#Returns a list of all cdx records of a website (also saves them in a text file)
def basicGetCdxRecords(url, filename): #works best for small scale queries only
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
        with open(filename,'w') as f:
            for record in data:
                f.write(f"{record}\n")
                allCdxRecords.append(record)
                # Each record represents an archived version
    else:
        print(f"Failed to retrieve data: {response.status_code}")
    return allCdxRecords

#Returns a list of all cdx records of a website, saves them in a textfile named according to the filename, and maintaint track of the progress of the progress so far in the progress_file to continue fetching records from where they were left
def getCdxRecords(url, filename, progress_file): #works for large-scale queries
    base_url = "https://web.archive.org/cdx/search/cdx"
    limit = 100000  # Limit per request
    params = {
        'url': url,
        'output': 'json',
        'matchType': 'prefix',
        'limit': limit,
        'showResumeKey': True, #The last entry returned is the resume key, which is then used to begin fetching records exactly from where they were left
        # 'pageSize': 1  # Smallest page size
    }

    # Load progress from the progress file
    resume_key = None
    if os.path.exists(progress_file): #checking the progress file to see whether a resume key exists to continue progress from
        with open(progress_file, 'r') as f:
            resume_key = f.read().strip()
    
    all_cdx_records = []
    while True:
        if resume_key:
            params['resumeKey'] = resume_key #updating the resume key
        
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            if not data:
                break
            # print("Fetched Data: ",data)
            
            # Write the records to the file and append to the list
            with open(filename, 'a') as f:
                for record in data[:-1]:  # Last item may be the resume key
                    f.write(f"{record}\n")
                    all_cdx_records.append(record)

            # Update the resume key and save it to the progress file
            resume_key = data[-1]
            print(f"Successfully fetched: {len(data)} records. Resume key: {resume_key}")
            with open(progress_file, 'w') as f:
                f.write(resume_key[0])
            
            # If no more results are available, exit the loop
            if 'resumeKey' not in params or not resume_key:
                break
            time.sleep(3) #To avoid sending too many requests to the server which then ends up refusing the connection
        else:
            print(f"Failed to retrieve data: {response.status_code}")

    return all_cdx_records

# #downloads all webpages inside the all_archives_versions folder 
def downloadArchivedVersions(fileWithRecords, archivedDirectory): #fileWithRecords is the name of the text file with all cdx records to download, archivedDirectory is the name of directory where to save all the web pages.

    wayback_base_url = "https://web.archive.org/web/"
    save_dir = archivedDirectory
    os.makedirs(save_dir, exist_ok=True)

    with open(fileWithRecords, 'r') as f:
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
url = "https://connect.facebook.net/signals/config/" #the url of the meta pixel
filename = "allPixelRecords.txt"
progress_file = "progress.txt"
cdx_records = getCdxRecords(url, filename, progress_file)

# downloadArchivedVersions(filename,'all_archived_versions')

