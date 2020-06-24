from time import sleep

from selenium import webdriver
import sys

from selenium.webdriver.common.by import By


def basic():
	driver = webdriver.Chrome(executable_path=sys.path[1] + '/Resources/chrodriver.exe')
	driver.get('https://opensource-demo.orangehrmlive.com/')
	sleep(2)
	driver.find_element(By.CSS_SELECTOR,'#txtUsername').send_keys('rajwinder')

basic()