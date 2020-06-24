import sys
import time
import unittest
from configparser import ConfigParser
from selenium import webdriver
import datetime
import pytest


# from Src.PageObject.Pages.LoginPage import LoginPage


class EnvironmentSetup():

	def configreader(self, factor, element):
		try:
			cfg = ConfigParser()
			cfg.read('F:\Pyhton\pytest_Car_Registration\Src\PageObject\config.ini')
			return cfg[factor][element]
		except FileNotFoundError as e:
			print('File not found', e)
		except Exception as e:
			print(e)

	def driver_setUp(self):

		if self.configreader('Default', 'browser') == 'chrome':
			self.driver = webdriver.Chrome('F:\Pyhton\pytest_Car_Registration\Resources\chrodriver.exe')
			print("------------------------------------------------------------------")
			print('Launching Chrome Driver')



		elif self.configreader('Default','browser')== ('firefox'):
		    self.driver = webdriver.Firefox('F:\Pyhton\pytest_Car_Registration\Resources/Resources/geckodriver.exe')
		    print("------------------------------------------------------------------")
		    print('Launching FireFox Driver')

		else:
			print('No driver Found')

		print('Run started at:', str(datetime.datetime.now()))
		self.driver.get(self.configreader('HomePage', 'url'))
		return self.driver


