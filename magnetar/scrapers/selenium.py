from time import sleep

class AbstractSelenium():

    # Need to put in customization for a user agent
    # https://stackoverflow.com/questions/29916054/change-user-agent-for-selenium-web-driver
    
    def __init__(self, driver_path = None):
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options
        
        self.driver_path = driver_path
            
    def build_scraper(self):
        '''
        Sets up the directory dependency to drop the save files into by default.
        '''

        import os

        if not os.path.exists('./html/'):
            os.mkdir('./html/')
        else: 
            print("/html/ directory exists")

        if not os.path.exists('./screenshot/'):
            os.mkdir('./screenshot/')
        else: 
            print("/screenshot/ directory exists")
            
    def launch_browser(self, options=None):
        from selenium import webdriver
        
        if not self.driver_path:
            service = webdriver.ChromeService(executable_path = '/usr/bin/chromedriver')
        else: 
            service = webdriver.ChromeService(executable_path = self.driver_path)
            
        self.driver = webdriver.Chrome(service=service)
        
    def close_browser(self):
        self.driver.close()
    
    def recaptcha_click(self):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support import expected_conditions as EC

        WebDriverWait(self.driver, 2).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[src^='https://www.google.com/recaptcha/api2/anchor']")))
        WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()

    def go_to_site(self, url, delay = 0):
        '''
        Instructs the chromedriver to navigate to the site.
        '''
        
        from time import sleep
        import re
        
        # The navigation will fail if it does not have a http:// or https:// prefix to the url. 
        # Only http:// needs to be appended because it will default to https if available from the site.
        s = url.strip()
        if re.search('https?\:\/\/', s) is not None:
            url_clean = s
        else:
            url_clean = f"http://{s}"
           
        # Check if there is a specified delay for navigation and act accordingly
        if delay > 0:
            sleep(delay)

        self.driver.get(url_clean)

    def save_source(self, filename):
        '''
        Saves down the source code for the current site that the driver is on. A one second sleep
        is granted to allow the site to load before it is saved.
        '''

        # from erebus.crypto import make_alphanumeric_token
        import time

        # rando_string = make_alphanumeric_token(15)

        # self.driver.get(url)
        time.sleep(1)
        file_out = f'./html/{filename}.html'
        print(file_out)

        with open(file_out, 'w', encoding='utf-8') as f: 
            f.write(self.driver.page_source)

    def screenshot(self, filename):
        '''
        Saves a screenshot of the current view of that url.
        '''
        self.driver.save_screenshot(f'./screenshot/{filename}.png')
    