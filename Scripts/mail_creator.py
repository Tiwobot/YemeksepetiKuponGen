from selenium import webdriver
from selenium.webdriver.common.by import By
import dependencies

PATH = dependencies.ChromeDriverLocation
driver = webdriver.Chrome(executable_path=PATH)
driver.get("https://generator.email/")
dependencies.tempMail = driver.find_element(By.ID, "email_ch_text").text
driver.close()