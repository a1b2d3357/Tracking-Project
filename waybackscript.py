from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_urls_from_page(driver):
    urls = []
    # Wait for the URLs to load
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'a')))
    
    # Find all 'a' tags and extract the 'href' attributes
    a_tags = driver.find_elements(By.TAG_NAME, 'a')
    print(a_tags)
    for a_tag in a_tags:
        try:
            href = a_tag.get_attribute('href')
            if "https://connect.facebook.net/signals/config/" in href:
                print(url)
                urls.append(href)
        except:
            pass
    
    return urls

def scrape_all_pages(base_url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")
    
    # Use WebDriver Manager to automatically manage ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    # First page
    driver.get(base_url)
    all_urls = get_urls_from_page(driver)
    
    # Check for and handle the next page
    try:
        while True:
            next_button = driver.find_element(By.LINK_TEXT, 'Next')
            if next_button:
                next_button.click()
                time.sleep(2)  # Give time for the next page to load
                page_urls = get_urls_from_page(driver)
                all_urls.extend(page_urls)
            else:
                break
    except Exception as e:
        print(f"No more pages to scrape: {e}")
    
    driver.quit()
    
    return all_urls

if __name__ == "__main__":
    # Base URL of the first page
    base_url = "https://web.archive.org/web/*/https://connect.facebook.net/signals/config/1264059003707256*"
    
    urls = scrape_all_pages(base_url)
    
    # Print all collected URLs
    for url in urls:
        print(url)