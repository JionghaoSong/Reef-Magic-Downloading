# Reef-Magic-Downloading


# Reef Magic Image Downloader

This script automates the process of downloading photos from the Reef Magic website, which operates day trips from Cairns to their advanced activity pontoon on the outer Great Barrier Reef. It leverages Selenium to access the webpage, locate image URLs, and download the images directly to a specified directory.

## Repository

You can find the repository [here](https://github.com/JionghaoSong/Reef-Magic-Downloading).

## Requirements

- Python 3.6+
- [Selenium](https://pypi.org/project/selenium/)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) (Make sure the version matches your Chrome browser)
- [Requests](https://pypi.org/project/requests/)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JionghaoSong/Reef-Magic-Downloading.git
   ```
2. Install required packages:
   ```bash
   pip install selenium requests
   ```
3. Ensure `chromedriver` is in your PATH or place it in the project directory.

## Usage

1. Open the script file and replace the placeholders:
   - `YOUR_URL_HERE` with the target URL on Reef Magic’s website.
   - `YOUR_DOWNLOAD_DIRECTORY_HERE` with the directory where you want to save the images.
2. Run the script:
   ```bash
   python reef_magic_downloader.py
   ```
3. The images will be saved in the specified directory.

## Script Overview

- Opens a browser via Selenium, navigates to the specified URL, and waits for the page to load.
- Finds all image thumbnails in the specified container.
- Downloads each image in high quality and saves it to the local directory.

## License

This project is open-source and available under the MIT License.
```

This README will guide users through setting up and running the script in your repository.
