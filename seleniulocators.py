from selenium import webdriver

# Create a new Chrome browser instance
driver = webdriver.Chrome()

# Open a webpage
driver.get("https://www.firefox.co.in")

# Verify the title of the webpage
expected_title = "GOOGLE"
actual_title = driver.title

if expected_title == actual_title:
    print("Title verification passed!")
else:
    print("Title verification failed!")

# Close the browser
driver.quit()