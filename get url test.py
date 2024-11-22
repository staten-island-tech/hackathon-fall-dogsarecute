import time
from selenium import webdriver

# Initialize WebDriver (make sure you have the correct path to your ChromeDriver)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # Update with the correct path

# Open a browser window (you can leave it blank or open a default page)
driver.get("about:blank")  # This will open a blank page

# Prompt the user to open the website
input("Please open the website in the browser and press Enter once you're ready...")

# Wait for the user to open the desired webpage
time.sleep(2)  # Optional, add more time if needed for the user to switch tabs

# Now capture the URL of the active tab
current_url = driver.current_url

print("URL of the active tab:", current_url)

# Close the browser after retrieving the URL
driver.quit()
