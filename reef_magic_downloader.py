from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os
import time

# Define the URL of the webpage
url = 'YOUR_URL_HERE'  # Replace with the actual URL

# Initialize Selenium WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed
driver.get(url)

# Wait for the page to load
time.sleep(5)  # Adjust wait time as needed

# Define the download directory
download_dir = 'YOUR_DOWNLOAD_DIRECTORY_HERE'
os.makedirs(download_dir, exist_ok=True)

# Locate all image download links in the photo-container section
photo_container = driver.find_element(By.ID, "photo-container")
thumbs = photo_container.find_elements(By.CLASS_NAME, "thumbs-thumb")

# Initialize image number
image_number = 1

total_photos = len(thumbs)
print(f"Found {total_photos} images, beginning download...")

for div in thumbs:
    try:
        # Find the download link
        link_tag = div.find_element(By.CLASS_NAME, "save-image")
        img_url = link_tag.get_attribute("href")

        # Download the image
        img_data = requests.get(img_url).content
        img_name = os.path.join(download_dir, f"image_{image_number}.jpg")

        with open(img_name, 'wb') as f:
            f.write(img_data)

        print(f"Downloaded {img_name} [{image_number}/{total_photos}]")

        # Increment image number
        image_number += 1
    except Exception as e:
        print(f"Error downloading image: {e}")

print("All images have been downloaded.")
driver.quit()
