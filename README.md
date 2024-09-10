# fcainfoweb-scrapper
Python based web scrapper for [fcainfoweb.nic.in/reports/Report_Menu_web.aspx](https://fcainfoweb.nic.in/reports/Report_Menu_Web.aspx) to extract wholesale and retail price reports from user defined year till present day

## Running the program:

### 1. Install Dependencies:
Assuming python is installed and configured properly
1. Selenium:<br/>
  `pip install selenium`<br/>
  Or alternatively use your desired package manager<br/>

2. Webdriver:<br/>
   The script uses mozilla's [GeckoDriver](https://github.com/mozilla/geckodriver) by default, make sure it is installed and configured properly.<br/>
   Those who wish to utilise a different driver make appropriate changes to `scrapper.py`.<br/>

### 2. Running:
Run the script with
`python scrapper.py -y year`<br/>
To Scrape wholesale data an optional flag `-w` is required<br/>
`python scrapper.py -w -y year`<br/>

**Example:**<br/>
To get retail data from 01/01/2024<br/>
`python scrapper.py -y 2024`<br/>
Wholesale date from same date:<br/>
`python scrapper.py -w -y 2024`

**Note:** default date starts from 1st of january for all years


