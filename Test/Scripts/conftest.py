import sys
import datetime
from Test.TestUtility.ExcelReader import Excel_Reader

import pytest
from selenium import webdriver

from Src.PageObject.Pages.HomePage import HomePage

from Src.Base.Setup import EnvironmentSetup



@pytest.yield_fixture(scope='function')
def setdriver():
	global driver
	driver =EnvironmentSetup().driver_setUp()

	yield driver
	print("------------------------------------------------------------------")
	print('Test Environment Destroyed')
	print('run Completed at:', str(datetime.datetime.now()))
	driver.quit()


@pytest.fixture(scope='function')
def go_to_registrationpage():
	HomePage(driver).register_link()




@pytest.yield_fixture(scope='function')
def input():
	print('in the fixture')
	yield
	print('teardown')