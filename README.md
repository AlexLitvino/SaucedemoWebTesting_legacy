# Objective

This is portfolio project for web testing of demo web site **Saucedemo**  

# Description

Link to web site: https://www.saucedemo.com/

Saucedemo is demo site that imitates online shop (login, listing items, adding to shopping cart, etc).  
Only run on Google Chrome browser is supported now.

# How to run tests
Get chromedriver for your Chrome browser version on [download page](https://chromedriver.chromium.org/downloads).
Unzip it and set path to chromedriver in [config.ini](config.ini) file instead of PUT_PATH_TO_CHROME_DRIVER_HERE line  
Install Allure (for example from [Git Hub repository](https://github.com/allure-framework/allure2/releases))   
Run `pip install -r requirements.txt`  
Run `python -m pytest --alluredir ./reports` or `python -m pytest -v --alluredir ./reports` for verbose output  
Run `allure generate -c ./reports` to generate report    
Run `allure serve ./reports` to display reports  