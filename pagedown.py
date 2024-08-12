import requests
import re
import os

def download_webpages(urls, output_folder):
    """
    Downloads webpages from a list of URLs and saves them to the specified output folder.
    The filenames will include a prefix based on the version number extracted from the URL.
    
    Args:
        urls (list of str): List of URLs to download.
        output_folder (str): Folder where the downloaded files will be saved.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check if the request was successful
            
            # Extract the version number from the URL
            match = re.search(r'v=([\d\.]+)', url)
            version = match.group(1) if match else 'unknown_version'
            
            # Generate the filename with prefix
            filename = f'Riteaid_{version}.html'
            file_path = os.path.join(output_folder, filename)
            
            # Save the content to a file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(response.text)
                
            print(f'Successfully downloaded {url} to {file_path}')
        
        except requests.RequestException as e:
            print(f'Failed to download {url}. Reason: {e}')
        except Exception as e:
            print(f'Error processing {url}. Reason: {e}')

def read_urls_from_file(file_path):
    """
    Reads URLs from a text file.
    
    Args:
        file_path (str): Path to the text file containing URLs.
    
    Returns:
        list: A list of URLs read from the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        urls = [line.strip() for line in file if line.strip()]
    return urls

# Path to the file containing URLs
url_file_path = 'riteaid_pixel.txt'
urls = read_urls_from_file(url_file_path)

output_folder = 'downloaded_webpages'
download_webpages(urls, output_folder)