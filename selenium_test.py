from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://localhost:8000/")

driver.maximize_window()

driver.find_element_by_id("username").send_keys("human")
driver.find_element_by_id("pass").send_keys("root")

driver.implicitly_wait(3)

driver.get_screenshot_as_file("devops71.png")

driver.find_element_by_id("submit").click()

driver.get_screenshot_as_file("devops72.png")

driver.quit()
