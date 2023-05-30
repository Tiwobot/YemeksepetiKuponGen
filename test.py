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

PATH = dependencies.ChromeDriverLocation
driver = webdriver.Chrome(PATH)

LinkString = "https://generator.email/katbabonova@maintecloud.com"

driver.get(LinkString)
title = driver.title
element = driver.find_element(
    By.XPATH, "//*[@id=\"email-table\"]/div[2]/div[4]/div[3]/center/div[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/th/a")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
print(driver.find_element(
    By.XPATH, "//*[@id=\"email-table\"]/div[2]/div[4]/div[3]/center/div[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/th/a").get_attribute("href"))
