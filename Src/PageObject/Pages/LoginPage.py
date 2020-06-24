from Src.Base.Setup import EnvironmentSetup
from selenium.webdriver.common.by import *

from Src.PageObject.PageLocators import Locator


class LoginPage(EnvironmentSetup):

#Locators


	def __init__(self, driver):
		self.driver =  driver
		self.Username = driver.find_element(By.XPATH,Locator.LP_XP_username)
		self.Password =driver.find_element(By.XPATH,Locator.LP_XP_Password)
		self.SubmitBtn = driver.find_element(By.XPATH, Locator.LP_XP_LoginBtn)
		self.RegistrationLink = driver.find_element(By.XPATH, Locator.LP_XP_RegistrationLink)



	def validUserLogin(self):
		self.Username.send_keys(self.configreader('LoginPage','username'))
		self.Password.send_keys(self.configreader('LoginPage','password'))
		self.SubmitBtn.click()








