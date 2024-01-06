# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# # Replace this with the path to your webdriver executable (e.g., chromedriver.exe)
# webdriver_path = 'path/to/chromedriver'

# # URL to navigate to
# url = 'https://www.nespresso.com/hu/en/csomagkovetes?orderId=28429496'

# # Set up the webdriver
# driver = webdriver.Chrome()
# driver.get(url)
# time.sleep(10)
# # XPath of the div element

# div_xpath = '//div[@direction="column"]'

# try:
#     # Locate the div element and click on it
#     div_element = driver.find_element(By.XPATH, div_xpath)
#     div_element.click()
#     time.sleep(2)
#     # Get all child elements with dynamic IDs under the div
#     child_elements = div_element.find_elements(By.XPATH, './/*[starts-with(@id, "react-select-2-option-")]')
#     print([i.text for i in child_elements])
#     # Iterate through each child element and click on its
#     m=0
#     for child_element in child_elements:
        
#         k = div_element.find_elements(By.XPATH, './/*[starts-with(@id, "react-select-2-option-")]')
#         k[m].click()
#         time.sleep(2)

#         driver.find_element(By.XPATH, div_xpath).click()
#         time.sleep(2)
#         #print([i.text for i in child_elements])
        

#         m=m+1
# finally:
#     # Close the browser window
#     time.sleep(15)
#     driver.quit()






import requests
from bs4 import BeautifulSoup

url = "https://intercars.pl/produkty/2128605-kranik-paliwa-all-balls-ab60-1079"

# Make a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the element with the specified class
    target_element = soup.find("div",class_="current-price-block voffset1 text-center")

    # Check if the element is found
    if target_element:
        # Get the text content of the element
        text_content = target_element.get_text(strip=True)

        # Print the text content
        print("Text Content:", text_content)
    else:
        print("Element not found with the specified class.")
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)
