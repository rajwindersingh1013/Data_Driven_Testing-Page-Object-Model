from selenium.webdriver.support.select import Select

from Src.Base.Setup import EnvironmentSetup



class BasicUtilities(EnvironmentSetup):
	def __init__(self,driver):
		self.driver =driver

	def select_from_DropDown(self,Webelement,selection ):
		Select(webelement).select_by_visible_text(selection)



