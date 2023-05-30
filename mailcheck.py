import time
import json
from typing import Self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from dependencies import dependencies


class MailChecker():
    def checkMail():

        PATH = dependencies.ChromeDriverLocation


        options = webdriver.ChromeOptions()

        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        driver = webdriver.Chrome(executable_path=PATH, options=options)
        driver.implicitly_wait(3)
        driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        useragentarray = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        ]

        for i in range(len(useragentarray)):
            driver.execute_cdp_cmd("Network.setUserAgentOverride", {
                               "userAgent": useragentarray[i]})
            print(driver.execute_script("return navigator.userAgent;"))

        LinkString = "https://generator.email/"+dependencies.tempMail

        driver.get(LinkString)
        title = driver.title
        print(title)
        element = driver.find_element(
            By.XPATH, "//*[@id=\"email-table\"]/div[2]/div[4]/div[3]/center/div[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/th/a")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        dependencies.AccountConfirmLink = driver.find_element(
            By.XPATH, "//*[@id=\"email-table\"]/div[2]/div[4]/div[3]/center/div[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/th/a").get_attribute("href")
        
