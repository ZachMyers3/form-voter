from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import random

import time


def vote(browser):
    browser.get("https://docs.google.com/forms/d/e/1FAIpQLSd_OjNQweI8xzyS8lCZUDX6Kb6hzOXYPuHxtTHNL9kdB2PZew/viewform")
    radiobuttons = browser.find_elements(By.CLASS_NAME, "docssharedWizToggleLabeledContainer")

    for button in radiobuttons:
        if "emma" in button.text.lower():
            button.click()

    try:
        submit = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Submit']")))
        submit.click() #this sometimes works but if so only once
    except Exception as e:
        print(str(e))
    
    time.sleep(0.5)

def main():
    option = webdriver.ChromeOptions()
    option.add_argument("-incognito")
    option.add_argument("headless")

    browser = webdriver.Chrome(options=option)
    vote_count = 1
    while True:
        # time.sleep(random.randrange(1, 3))
        vote(browser=browser)
        print(f"Voted {vote_count} times!")
        vote_count += 1


if __name__ == "__main__":
    main()

