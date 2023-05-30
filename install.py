from selenium import webdriver
import chromedriver_autoinstaller


chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title