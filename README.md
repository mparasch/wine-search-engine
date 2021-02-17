# wine-search-engine
## Description
This project is intended to allow for an easy way to scrape wine data from [wine.com](https://www.wine.com/list/wine/7155) based on the criteria selected by the user. A simple GUI has been created so that even a non technical user can use the tool. The data is exported to a CSV file in the active directory.\
This project be a useful tool for someone looking to analyze wine data or the casual wine connoisseur!

## GUI Visual
![GUI visual](/images/GUI_example.JPG)

## Installation
### Requirements
* Python 3
* Libraries:
    * urllib.request
    * bs4
    * pandas
    * tkinter
If you do not have any of these libraries, you can install them using ```pip install <library or module name>```.
## Usage
If you run the ```Wine_Data.py``` file, it will produce an interface to select the criteria you want (price and rating). Once selected, press "Create Wine List" and a CSV file will be created in the same directory titled witha  description of the criteria and date. The CSV file will contain the following values for each wine identified: name, wine_type, origin, rating, reviews, sale_price, savings, savings_percent.

## Project Status
I do not plan on contributing or adding to this project.
