from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.action_chains import ActionChains
import time
import getpass
import os
import ctypes

homeProfile = "C:\\Users\\wethe\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\3y2zy2pp.default"
workProfile = "C:\\Users\\Administrator\\AppData\\Roaming\Mozilla\\Firefox\\Profiles\\6q068ubt.default-1453236670223"
tabletProfile = "C:\\Users\\Owner\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\bohrazcl.default"
#profile = FirefoxProfile(tabletProfile)

driver = webdriver

def Login():
	global driver
	try:
		username = input("Username: ")
		password = getpass.getpass()
		os.system("cls")
		print("Logging In")
		# Select TMCC
		driver.get("https://sso.nevada.edu/landing.php")
		driver.find_element_by_xpath("//img[@alt='TMCC']").click()
		time.sleep(10)
		elem = driver.find_element_by_id("okta-signin-username")
		elem.clear()
		elem.send_keys(username)
		elem = driver.find_element_by_id("okta-signin-password")
		elem.clear()
		elem.send_keys(password)
		elem.send_keys(Keys.ENTER)
		time.sleep(10)
		if (driver.title == "Nevada System of Higher Education (Hub) - My Applications"):
			print("Logged in")
		else:
			print("Login failed")
			Login()
	except:
		print("Error. Please try again")
		Login()
	
def CheckIn():
	global driver
	print("Navigating to Check in page")
	# Enter Time page
	driver.get("https://www.myworkday.com/nshe/d/home.htmld#selectedWorklet=501%24162")
	time.sleep(10)
	# Active NSHE member
	driver.find_element_by_xpath("//div[@tabindex='-2']").click()
	time.sleep(10)
	print("Checking in")
	# Check in button
	driver.find_element_by_id("wd-DropDownCommandButton-56$234380").click()
	time.sleep(10)
	actions = ActionChains(driver)
	actions.send_keys('Student Hours Worked')
	actions.perform()
	actions = ActionChains(driver)
	actions.send_keys(Keys.ENTER)
	actions.perform()
	time.sleep(10)
	driver.find_element_by_xpath("//button[@title='OK']").click()
	time.sleep(10)
	driver.find_element_by_xpath("//button[@title='Done']").click()

def CheckOut():
	global driver
	print("Navigating to Check in page")
	# Enter Time page
	driver.get("https://www.myworkday.com/nshe/d/home.htmld#selectedWorklet=501%24162")
	time.sleep(10)
	# Active NSHE member
	driver.find_element_by_xpath("//div[@tabindex='-2']").click()
	time.sleep(10)
	print("Checking out")
	driver.find_element_by_xpath("//button[@title='Check Out']").click()
	time.sleep(10)
	driver.find_element_by_xpath("//input[@id='gwt-uid-7']").click()
	driver.find_element_by_xpath("//button[@title='OK']").click()
	time.sleep(10)
	driver.find_element_by_xpath("//button[@title='Done']").click()

def LogOut():
	global driver
	print("Logging out")
	driver.find_element_by_class_name("WGMH").click()
	driver.find_element_by_class_name("WLCI").click()
	time.sleep(3)
	driver.close()
	os.system("cls")

def AltTab():
	ctypes.windll.user32.keybd_event(0x12, 0, 0, 0) #Alt
	ctypes.windll.user32.keybd_event(0x09, 0, 0, 0) #TAB
	ctypes.windll.user32.keybd_event(0x09, 0, 2, 0) #~Tab
	ctypes.windll.user32.keybd_event(0x12, 0, 2, 0) #~Alt

def Menu():
	global driver
	os.system("cls")
	print("(1) - Check in")
	print("(2) - Check out\n")
	selection = input("Selection: ")
	# Check in
	if (selection == '1'):
		driver = driver.Chrome()
		AltTab()
		#driver.set_window_position(-3000, 0)
		Login()
		time.sleep(10)
		CheckIn()
		time.sleep(10)
		driver.set_window_position(0, 0)
		time.sleep(20)
		LogOut()
	# Check Out
	elif (selection == '2'):
		driver = driver.Chrome()
		AltTab()
		#driver.set_window_position(-3000, 0)
		Login()
		time.sleep(10)
		CheckOut()
		time.sleep(10)
		driver.set_window_position(0, 0)
		time.sleep(20)
		LogOut()

while(True):
	Menu()


