import unittest
import time
from argparse import Action

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Src.Base.Setup import EnvironmentSetup
from Src.PageObject.Pages.HomePage import HomePage
from Src.PageObject.Pages.LoginPage import LoginPage


class Tests_DragDrop(EnvironmentSetup):
	@pytest.fixture
	def setUp(self):
		self.driver =self.driver_setUp()
		self.driver.get("https://opensource-demo.orangehrmlive.com/")
		self.driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys('Admin')
		self.driver.find_element(By.XPATH, "//input[@id='txtPassword']").send_keys("admin123")
		self.driver.find_element(By.XPATH, "//input[@id='btnLogin']").click()
		time.sleep(2)


	def test_mouseMovement_and_Select(self,setUp):
		actions =ActionChains(self.driver)
		Admin = self.driver.find_element(By.XPATH,"//b[contains(text(),'Admin')]")
		Usermanagement = self.driver.find_element(By.XPATH,"//a[@id='menu_admin_UserManagement']")
		Users = self.driver.find_element(By.XPATH,"//a[@id='menu_admin_viewSystemUsers']")

		actions.move_to_element(Admin).move_to_element(Usermanagement).click(Users).perform()
		time.sleep(2)


		UserRole = self.driver.find_element(By.XPATH,"//select[@id='searchSystemUser_userType']")

		Select(UserRole).select_by_visible_text('ESS')






