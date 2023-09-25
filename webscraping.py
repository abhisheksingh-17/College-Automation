import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Create Chrome options
chrome_options = Options()

# Initialize Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the webpage containing the list of universities
driver.get('https://www.stilt.com/blog/2018/01/top-100-us-universities-computer-science/')

# Find all the <td> elements that contain university names using the correct method
university_td_elements = driver.find_elements(By.CSS_SELECTOR, 'td')

# Extract the text (university names) from the <td> elements and clean them using regex
universities = [re.sub(r'\[[^\]]*\]|\d+|No|R-Rank|S-Rank|Institution Name', '', element.text.strip()) for element in university_td_elements]

# Remove empty strings (if any) from the list
universities = [uni.strip() for uni in universities if uni.strip()]

# Create a DataFrame from the collected university names
df = pd.DataFrame({'University Name': universities})

# Save the data to an Excel file
df.to_excel('Top_100_US_Universities_for_Computer_Science.xlsx', index=False)

# Close the WebDriver
driver.quit()
