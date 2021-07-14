'''
3. Create a test case for Help search using python & selenium script

Test Case:
User can search for solutions of Cancelling an order on Amazon
1. Open Amazon Help page https://www.amazon.com/gp/help/customer/display.html
2. Use “Search Help Library” field and search for Cancel order:
3. Emulate hitting keyboard ENTER btn with send_keys command (here’s how)
4. Verify that ‘Cancel Items or Orders’ text is present

'''



# Use “Search Help Library” field and search for Cancel order:
# element = driver.find_element(By.ID, 'helpsearch')
# element.send_keys('cancel order')
# element.send_keys(Keys.RETURN)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/Users/seashore/Dropbox/My Mac (MacBook-Air.lan)/Desktop/chromedriver')
#Open Amazon Help page https://www.amazon.com/gp/help/customer/display.html
driver.get('https://www.amazon.com/gp/help/customer/display.html')
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.ID, 'helpsearch').send_keys('Cancel Order', Keys.RETURN)

actual_text = driver.find_element(By.CSS_SELECTOR, '.help-content h1').text
expected_text = 'Cancel Items or Orders'


assert expected_text == actual_text, f'Expected {expected_text}, but got{actual_text}'

driver.quit()

