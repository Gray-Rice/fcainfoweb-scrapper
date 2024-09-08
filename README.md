# fcainfoweb-scrapper
Python based web scrapper for [fcainfoweb.nic.in/reports/Report_Menu_web.aspx](https://fcainfoweb.nic.in/reports/Report_Menu_Web.aspx) to extract wholesale and retail price reports from user defined year till present day

## Running the program:

### 1. Install Dependencies:
Assuming python is installed and configured properly
1. Selenium:<br/>
  `pip install selenium`<br/>
  Or alternatively use your desired package manager<br/>

2. Webdriver:<br/>
   The script use mozilla's [GeckoDriver](https://github.com/mozilla/geckodriver) by default, make use it is installed and configured properly.<br/>
   Those who wish to utilise a different driver make appropriate changes to `scrapper.py`.<br/>

### 2. Running:
Run the script with
`python scrapper.py`<br/>

**Linux only:**<br/>
Using `tee` to save logs<br/>
`python -u scrapper.py | tee -a log.txt`
