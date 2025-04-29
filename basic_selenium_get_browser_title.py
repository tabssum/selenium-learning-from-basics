from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.tutorialspoint.com")

   # Get the actual title of the page
title = driver.title

   # Print the title of the website
print("Title: " + title)
    
   # Close the browser window
driver.quit()
