
from Src.Base.Setup import EnvironmentSetup
from selenium.webdriver.common.by import By

from Src.PageObject.PageLocators import Locator
from Src.PageObject.Pages.RegistrationPage import RegistrationPage


class HomePage:

	def __init__(self, driver):
		self.driver = driver
		self.__RegisterLink =self.driver.find_element(By.XPATH,"//button[contains(text(),'New')]")

	def register_link(self):
		self.__RegisterLink.click()
		return RegistrationPage
