from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Set up Chrome WebDriver (Ensure you have Chrome and ChromeDriver installed)
driver = webdriver.Chrome('X:\\Laptop Stuff\\Softwares\\Coding\\Software\\chromedriver-win64\\chromedriver.exe')  # Replace with the path to your chromedriver executable

# Navigate to the website
driver.get('https://www.usnews.com/best-graduate-schools/top-science-schools/computer-science-rankings')

# Create an empty list to store the data
professors_data = []

# Find and loop through the "Next" button to navigate through multiple pages
while True:
    # Find the table containing the list of computer science professors
    professors_table = driver.find_element(By.CLASS_NAME, 'SortableTablestyles__StyledTable-sc-12knbw7-0')

    # Iterate through each row in the table
    for row in professors_table.find_elements(By.TAG_NAME, 'tr'):
        columns = row.find_elements(By.TAG_NAME, 'td')
        if len(columns) >= 4:  # Ensure the row has enough columns (including email)
            professor_name = columns[0].text
            department = columns[1].text
            mobile_no = columns[2].text
            email = columns[3].text  # Modify this to extract email
            professors_data.append([professor_name, department, mobile_no, email])

    # Check if there is a "Next" button to go to the next page
    next_button = driver.find_element(By.PARTIAL_LINK_TEXT, 'Next')
    if 'disabled' in next_button.get_attribute('class'):
        break  # No more pages, exit the loop
    else:
        next_button.click()  # Go to the next page
        time.sleep(2)  # Optional: Add a delay to allow the page to load

# Create a DataFrame from the collected data
df = pd.DataFrame(professors_data, columns=['Name of the Professor', 'Department', 'Mobile No', 'Email'])

# Save the data to an Excel file
df.to_excel('Computer_Science_Professors.xlsx', index=False)

# Close the WebDriver
driver.quit()
