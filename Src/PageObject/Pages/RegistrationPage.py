from _pytest import unittest

from Src.Base.Setup import EnvironmentSetup
from selenium.webdriver.common.by import By

from Src.PageObject.PageLocators import Locator


class RegistrationPage:

	def __init__(self, driver):
		self.driver = driver
		self.__data = driver.find_elements(By.CSS_SELECTOR, "#table1 tr td :last-child")
		self.__message=driver.find_element(By.XPATH,"//p[@id='message']")


	def new_Registration(self, datalist):

		for x in range(8):
			self.__data[x].send_keys(datalist[x])

		self.__data[8].click()

	def message_displayed(self):
		return self.__message.text