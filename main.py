import time
from dependencies import dependencies
from mailgen import MailGenerator
import yemeksepeti_mail 
import yemeksepeti_creator 
from mailcheck import MailChecker

MailGenerator.generateAndSet()
yemeksepeti_creator.yemeksepetiCreator()