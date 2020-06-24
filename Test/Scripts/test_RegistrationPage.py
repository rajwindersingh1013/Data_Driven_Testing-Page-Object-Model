import pytest
from HtmlTestRunner import HTMLTestRunner
from _pytest import unittest
from selenium import webdriver


from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Src.Base.Setup import EnvironmentSetup
from Src.PageObject.Pages.HomePage import HomePage
from Src.PageObject.Pages.LoginPage import LoginPage
from Src.PageObject.Pages.RegistrationPage import RegistrationPage
from Test.TestUtility.ExcelReader import Excel_Reader


ndata= Excel_Reader("NegativeCases").getfulldata()

pdata= Excel_Reader("PositiveCases").getfulldata()




		#RegistrationPage = HomePage(driver).register_link()


@pytest.mark.parametrize("data", pdata)
def test_Positivecases(setdriver, go_to_registrationpage, data):
	driver = setdriver
	RegistrationPage(driver).new_Registration(data)
	currenturl = driver.current_url
	displayurl = EnvironmentSetup().configreader('DisplayPage', 'url')
	assert currenturl == displayurl


@pytest.mark.parametrize("data", ndata)
def test_Negativecases( setdriver, go_to_registrationpage, data):
	driver = setdriver
	RegistrationPage(driver).new_Registration(data)
	print(ndata[8])
	msg = RegistrationPage(driver).message_displayed()
