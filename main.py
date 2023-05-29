from dependencies import dependencies
from mailgen import MailGenerator
import yemeksepetiLogger 
from mailcheck import MailChecker

MailGenerator.generateAndSet()
yemeksepetiLogger.yemeksepetiCreateAccount()
MailChecker.checkMail()
