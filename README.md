# Wine Web Scraper Application

## Overview
The Wine Scraper Application is a Python-based tool that scrapes wine data from the Wine.com website based on user-specified criteria. The application uses a GUI (Graphical User Interface) built with Tkinter for easy interaction. The data is processed using the BeautifulSoup library and saved as a CSV file for further analysis.

## Features
- Scrape wine data including name, type, origin, ratings, reviews, price, and discounts.
- Filter wines based on minimum ratings and maximum price.
- Generate a CSV report with the scraped data.
- Simple and interactive GUI.
Follow these steps to set up and run the application:


## Setup and Installation

### Prerequisites
Ensure you have Python installed. You will also need the following Python libraries:
- `urllib` (standard library, no need to install)
- `BeautifulSoup` (from the `bs4` package)
- `pandas`
- `tkinter` (standard library, no need to install)

### Install Dependencies
1. **Clone the repository**:
  ```bash
   git clone https://github.com/mparasch/wine-search-engine.git
   cd wine-search-engine
  ```
2. **Install Dependencies**
```bash
pip install beautifulsoup4 pandas
```
3. Configure the API key:
* Sign up at RapidAPI to obtain an API key for the Deezer API.
* Open the app.py file.
* Replace <INSERT deezer API KEY> in the get_songList function with your API key.

4. Run the application
  ```bash
   python app.py
  ```

## GUI Visual
![GUI visual](/images/GUI_example.JPG)
