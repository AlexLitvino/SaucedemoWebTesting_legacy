# SaucedemoWebTesting

## Objective

This is portfolio project for web testing of demo web site **Saucedemo**  

## Description

Link to web site: https://www.saucedemo.com/

Saucedemo is demo site that imitates online shop (login, listing items, adding to shopping cart, etc).  
Only run on Google Chrome browser is supported now.

## Supported browsers
- Google Chrome
- Firefox
- MS Edge

## How to run tests
- Get driver for required browser and version:  
    - chromedriver for Chrome browser on [downloads page](https://chromedriver.chromium.org/downloads).
    - geckodriver for Firefox browser on [releases page](https://github.com/mozilla/geckodriver/releases)  
    - edgedriver for Edge browser on [downloads page](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/#downloads)  
    NOTE: By default driver named "msedgedriver.exe" but Selenium looking for default name "MicrosoftWebDriver.exe", so downloaded executable should be renamed 
- Unzip it and add driver location directory to PATH variable
- Install Allure (for example from [Git Hub repository](https://github.com/allure-framework/allure2/releases)) and add its `\bin` directory to PATH variable   
- Run `pip install -r requirements.txt` to install required libraries  
- Run `python -m pytest --alluredir ./reports` to run all tests  
- Run `allure generate -c ./reports` to generate report  
- Run `allure serve ./reports` to display reports  
