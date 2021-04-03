from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://localhost:8000/")

driver.maximize_window()

driver.find_element_by_id("username").send_keys("human")
driver.find_element_by_id("pass").send_keys("root")

driver.implicitly_wait(3)

driver.find_element_by_id("submit").click()

print("Test Done Successfully.")

driver.quit()
