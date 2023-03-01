from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import random

import time


def vote():
    option = webdriver.ChromeOptions()
    option.add_argument("-incognito")

    browser = webdriver.Chrome(options=option)

    browser.get("https://docs.google.com/forms/d/e/1FAIpQLSd_OjNQweI8xzyS8lCZUDX6Kb6hzOXYPuHxtTHNL9kdB2PZew/viewform")
    radiobuttons = browser.find_elements(By.CLASS_NAME, "docssharedWizToggleLabeledContainer")

    for button in radiobuttons:
        if "emma" in button.text.lower():
            print(button)
            button.click()

    try:
        submit = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Submit']")))
        submit.click() #this sometimes works but if so only once
    except Exception as e:
        print(str(e))
    
    time.sleep(1)

def main():
    while True:
        time.sleep(random.randrange(2, 5))
        vote()


if __name__ == "__main__":
    main()

