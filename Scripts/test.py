import time
import json
from typing import Self
import winsound
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from yemeksepeti_scraper import YS_signup_mailStep, YS_signup_secondPhase
from mail_scraper import checkexistingMails, scrapeNewMail
from data_manager import get_mail_authLink, set_mail_authLink, get_mailAddress, get_mailLink, set_mailAddress
import random
from datetime import timedelta
from datetime import datetime
import string
import secrets

scrapeNewMail()
