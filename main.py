from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import getpass
import os
import ctypes
from notify import Email

homeProfile = "C:\\Users\\wethe\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\3y2zy2pp.default"
workProfile = "C:\\Users\\Administrator\\AppData\\Roaming\Mozilla\\Firefox\\Profiles\\6q068ubt.default-1453236670223"
tabletProfile = "C:\\Users\\Owner\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\bohrazcl.default"
#profile = FirefoxProfile(tabletProfile)

email = ""
driver = ""

def Login():
	global driver, email
	driver = webdriver.Chrome()
	AltTab()
	try:
		username = input("Username: ")
		password = getpass.getpass()
		email = username + "@tmcc.edu"
		os.system("cls")
		print("Logging In")
		# Select TMCC
		driver.get("https://sso.nevada.edu/landing.php")
		try:
			tmcc = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.XPATH, "//img[@alt='TMCC']")))
			tmcc.click()
		except:
			print("TMCC Not found")
			Login()
		try:
			elem = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.ID, "okta-signin-username")))
			elem.clear()
			elem.send_keys(username)
			elem = driver.find_element_by_id("okta-signin-password")
			elem.clear()
			elem.send_keys(password)
			elem.send_keys(Keys.ENTER)
		except:
			print("Could not find username/password field")
			Login()
		try:
			success = WebDriverWait(driver, 45).until(EC.title_is(("Nevada System of Higher Education (Hub) - My Applications")))
			print("Logged in")
		except:
			print("Login Failed")
	except:
		print("Error. Please try again")
		Login()
	
def CheckIn():
	global driver
	print("Navigating to Check in page")
	# Enter Time page
	driver.get("https://www.myworkday.com/nshe/d/home.htmld#selectedWorklet=501%24162")
	# Active NSHE member
	try:
		activeNshe = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.XPATH, "//div[@tabindex='-2']")))
		activeNshe.click()
	except:
		print("Could not select 'Active NSHE Member'")
		CheckIn()
	print("Checking in")
	# Check in button
	try:
		checkInButton = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.ID, "wd-DropDownCommandButton-56$234380")))
		checkInButton.click()
	except:
		print("Could not click 'Check in'")
		CheckIn()
	time.sleep(10)
	actions = ActionChains(driver)
	actions.send_keys('Student Hours Worked')
	actions.perform()
	actions = ActionChains(driver)
	actions.send_keys(Keys.ENTER)
	actions.perform()
	try:
		okButton = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.XPATH, "//button[@title='OK']")))
		okButton.click()
		doneButton = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.XPATH, "//button[@title='Done']")))
		doneButton.click()
	except:
		print("Could not check in")
		CheckIn()
	try:
		print("Emailing Status")
		checkTime = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.XPATH, "//div[@id='promptOption-gwt-uid-2']")))
		print("Last successful checkin: " + checkTime.text)
		Email(email, checkTime.text)
	except:
		print("Could not send email")


def CheckOut():
	global driver
	print("Navigating to Check in page")
	# Enter Time page
	driver.get("https://www.myworkday.com/nshe/d/home.htmld#selectedWorklet=501%24162")
	# Active NSHE member
	try:
		activeNshe = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.XPATH, "//div[@tabindex='-2']")))
		activeNshe.click()
	except:
		print("Could not select 'Active NSHE Member'")
		CheckOut()
	print("Checking out")
	try:
		checkOutButton = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.XPATH, "//button[@title='Check Out']")))
		checkOutButton.click()
		clockOutRadio = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.XPATH, "//input[@id='gwt-uid-7']")))
		clockOutRadio.click()
		okButton = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.XPATH, "//button[@title='OK']")))
		okButton.click()
		doneButton = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.XPATH, "//button[@title='Done']")))
		doneButton.click()
	except:
		print("Could not check out")
		CheckOut()
	try:
		print("Emailing Status")
		checkTime = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.XPATH, "//div[@id='promptOption-gwt-uid-2']")))
		print("Last successful checkin: " + checkTime.text)
		Email(email, checkTime.text)
	except:
		print("Could not send email")

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
	time.sleep(.1)
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
		#driver.set_window_position(-3000, 0)
		#driver.set_window_size(500,500)
		#driver.set_window_position(0, 0)
		#AltTab()
		Login()
		CheckIn()
		time.sleep(25)
		LogOut()
	# Check Out
	elif (selection == '2'):
		#driver.set_window_position(-3000, 0)
		#driver.set_window_size(500,500)
		#driver.set_window_position(0, 0)
		#AltTab()
		Login()
		CheckOut()
		time.sleep(25)
		LogOut()

while(True):
	Menu()



