import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Replace 'path/to/chromedriver' with the path to your ChromeDriver executable
driver_path = 'path/to/chromedriver'
driver = webdriver.Chrome()

# Open the YouTube link (replace with your desired link)
url = 'https://www.youtube.com/@CodingShiksha/videos'
driver.get(url)
time.sleep(10)
# Simulate pressing the Page Down key 200 times
for _ in range(200):
    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1.5)  # Adjust sleep time based on your network speed and page loading time

# Find all video links using XPath
video_links = driver.find_elements(By.XPATH,'//a[@id="video-title-link"]')

# Extract data and write to CSV
csv_file_path = 'youtube_data.csv'

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Name', 'Time','Link'])

    for link in video_links:
        href = link.get_attribute('href')
        aria_label = link.get_attribute('aria-label')

        if aria_label:
            name, time_ago = aria_label.split('ago')
            csv_writer.writerow([name, time_ago, href])

# Close the browser
driver.quit()
