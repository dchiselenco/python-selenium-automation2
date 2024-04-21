from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open https://www.target.com/
driver.get('https://www.target.com/')
sleep(6)


# Click SignIn button
#data-test="@web/AccountLink"
#$x("//a[@data-test='@web/AccountLink']")
driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
sleep(4)


# Click SignIn from side navigation
#$x("//a[@data-test='accountNav-signIn']")
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
sleep(4)


#“Sign into your Target account” text is shown
# $x("//span[text(), 'Sign into your Target account']")
# $x("//h1[contains(@class, 'styles__AuthHeading')]//span")
# print(actual_text)
#actual_text = driver.find_element(By.XPATH,"//h1[contains(@class, 'styles__AuthHeading') and .//span[contains(text(), 'Sign into your Target account')]]").text
#print(actual_text)


expected = 'Sign into your Target account'
actual = driver.find_element(By.XPATH,"//h1[contains(@class, 'styles__AuthHeading') and .//span[contains(text(), 'Sign into your Target account')]]").text
assert expected == actual, f'Expected {expected} did not match actual {actual}'


# driver.find_element(by=By.XPATH, "//span[text()='Sign into your Target account']")

# Make sure login button is shown
driver.find_element(By.ID, 'login' )
